import discord
from discord.ext import commands
import requests
from PIL import Image
from models.clouds import *
from io import BytesIO


class IdCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cloud(self, ctx):
        img_url = ctx.message.attachments[0].proxy_url 
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content)) #get image 
        pred = predict(model, img, should_log=True)
        await ctx.send(pred)
    
async def setup(bot):
    await bot.add_cog(IdCog(bot))
