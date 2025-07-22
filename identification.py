import discord
import random
from discord.ext import commands
import requests
from PIL import Image
from models.clouds import *
from io import BytesIO
import json
import imghdr

with open("whatis.json") as f:
    info = json.load(f)


abbreviations_dict = {}
full_to_abbr = {}
abbreviations_str = ""
for i in range(11):
    abbreviations_dict[info['cloud_names'][i]] = info['cloud_names'][i + 11]
    abbreviations_str += f"{info['cloud_names'][i + 11]}: {info['cloud_names'][i]}, "
    full_to_abbr[info['cloud_names'][i + 11]] = info['cloud_names'][i][0].upper() + info['cloud_names'][i][1]
abbreviations_str = f"[{abbreviations_str[:-2]}]"

class IdCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cloudId(self, ctx):
        try:
            img_url = ctx.message.attachments[0].proxy_url 
            response = requests.get(img_url)

            content_type = response.headers.get("Content-Type", "")

            if "image" not in content_type:
                await ctx.send("I'm sorry! I don't recognize that as an image")
                return

            img_bytes = BytesIO(response.content)
            img = Image.open(img_bytes)
                
            preds = predict(model, img, should_log=True)
            #Stuff that should be kind of like hyperparams
            confidence_thres = 0.15
            confident = True

            for pred in [key for key in preds.keys()][:1]:
                if preds[pred].item() <= confidence_thres:
                    confident = False
                

            ret = "Here is what the model thinks the clouds in the picture most likely are, alongside its confidence.\n"
            ret += "-" * 20 + "\n"
            for pred in preds.keys():
                ret += f"{str(pred)} : {str(round(preds[pred].item(), 3))}" + "\n"
            ret += "-" * 20 + "\n"

            if not confident:
                ret += "The model doesn't seem to be very confident in any of its predictions. This can be due to the photo being not optimal (with multiple types of clouds, blurry, etc). You could try taking another photo, or calling !info [cloudname] in order to get more info and manually identify them."
            await ctx.send(ret)

        except IndexError:
            await ctx.send("Please attach an image!")
        except Exception as e:
            print(Exception)
            await ctx.send("I'm sorry! There was an error processing the image. Please make sure that it is an extension 'jpeg', 'png', 'jpg', or 'webp'")
        
    @commands.command()
    async def info(self, ctx, cloud_name : str, num_to_send=3):
        cloud_name = cloud_name.lower()

        if cloud_name not in info["cloud_names"]:
            await ctx.send("Please send your info command as !info [cloudName]. For a list of valid cloudnames, please do !cloudnames")
            return
        if cloud_name in abbreviations_dict:
            cloud_name = abbreviations_dict[cloud_name]

        cloud_files = []
        selected_file_nums = random.sample([i for i in range(info["decent_imgs"][full_to_abbr[cloud_name]][0])], num_to_send)
        for num in selected_file_nums:
            fp = f"models/data/cloud_data/{full_to_abbr[cloud_name]}/{full_to_abbr[cloud_name]}-N{str(num).rjust(3, '0')}.jpg"
            cloud_files.append(discord.File(fp)) 
        await ctx.send(info["cloud_info"][cloud_name] + "\n Here are some images", files=cloud_files)

    @commands.command()
    async def cloudnames(self, ctx):
        await ctx.send("Here is a list of valid cloud names and their abbreviations!:\n" + abbreviations_str, files=discord.File("cloud_altitudes.png"))


async def setup(bot):
    await bot.add_cog(IdCog(bot))
