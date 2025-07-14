from models.clouds import *
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_model()
load_dotenv()
bot_key = os.getenv('bot_key')
my_guild_name = os.getenv('my_server_name')

class NatBot(commands.Bot):
    def __init__(self):
        intents= discord.Intents.default()
        intents.message_content = True #let em read the messages 
        super().__init__(command_prefix = "!", intents=intents) #Basically now creates a bot kind of like in the learning but now we subclassing

    #No more wrappers!
    async def on_read(self):
        print("NatBot is ready to go!")


if __name__ == "__main__":
    bot = NatBot()
        #or less of them :sob: 
    @bot.command()
    async def ping(ctx): #when user types prefix + fxn name (so in this case !ping). Also gives it the context which holds metadata
        await ctx.send("pong!")


    bot.run(bot_key)

