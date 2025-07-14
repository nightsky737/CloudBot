import discord
from discord.ext import commands
import requests
from PIL import Image
from models.clouds import *
from io import BytesIO

load_model()

class IdCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cloud(ctx):
        img_url = ctx.message.attachments[0].proxy_url 
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content)) #get image 
        #i want to avoid downloading to compute
        pred = predict(model, img, should_log=False)
        await ctx.send(pred)
    
    
