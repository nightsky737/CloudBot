import discord
from discord.ext import commands
import requests
from PIL import Image
from models.clouds import *
from io import BytesIO
import json

with open("whatis.json") as f:
    info = json.load(f)


abbreviations_dict = {}
abbreviations_str = ""
for i in range(11):
    abbreviations_dict[info['cloud_names'][i]] = info['cloud_names'][i + 11]
    abbreviations_str += f"{info['cloud_names'][i + 11]}: {info['cloud_names'][i]}, "
abbreviations_str = f"[{abbreviations_str[:-2]}]"


class IdCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cloudId(self, ctx):
        img_url = ctx.message.attachments[0].proxy_url 
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content)) #get image 
        pred = predict(model, img, should_log=True)
        await ctx.send(pred)
    
    @commands.command()
    async def info(self, ctx, cloud_name : str):
        cloud_name = cloud_name.lower()

        if cloud_name not in info["cloud_names"]:
            await ctx.send("Please send your info command as !info [cloudName]. For a list of valid cloudnames, please do !cloudnames")
            return
        if cloud_name in abbreviations_dict:
            cloud_name = abbreviations_dict[cloud_name]

        await ctx.send(info["cloud_info"][cloud_name])

    @commands.command()
    async def cloudnames(self, ctx):
        await ctx.send("Here is a list of valid cloud names and their abbreviations!:\n" + abbreviations_str)

async def setup(bot):
    await bot.add_cog(IdCog(bot))
