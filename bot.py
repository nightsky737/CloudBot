import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json

class NatBot(commands.Bot):
    def __init__(self):
        intents= discord.Intents.default()
        intents.message_content = True #let em read the messages 
        super().__init__(command_prefix = "!", intents=intents) #Basically now creates a bot kind of like in the learning but now we subclassing

    #No more wrappers!
    async def on_ready(self):
        print("NatBot is ready to go!")

    async def setup_hook(self):
        await self.load_extension("identification") 

    async def help(self, ctx):
        help_msg = '''
        I'm Nat, short for NatBot 🌱  
        I can identify:
        - ☁️ Cloud types using `!cloud` + image attachment  
        - 🐾 Animals (i didnt get around to this yet) using `!animal`  
        - 🌿 Plants (hopefully) using `!plant`  

        Ex:
        !cloud  and
        '''
        await ctx.send(help_msg)

if __name__ == "__main__":
     
    load_dotenv()
    bot_key = os.getenv('bot_key')
    my_guild_name = os.getenv('my_server_name')

    with open("whatis.json", 'r') as f:
        cloud_info = json.load(f)
    bot = NatBot()


 #or less of them i dont know what im doing :sob: 
    @bot.command()
    async def ping(ctx): #when user types prefix + fxn name (so in this case !ping). Also gives it the context which holds metadata
        await ctx.send("pong!")
    
    @bot.command()
    async def whatis(ctx, question):
        #Just gives a definition of what that word is 
        question = question.lower()

        if cloud_info.get(question):
            msg = cloud_info[question]
        else:
            msg = "Sorry! I don't recognize that cloud type"
        await ctx.send(msg)

    bot.run(bot_key)

