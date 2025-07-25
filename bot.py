import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json

class NatBot(commands.Bot):
    def __init__(self):
        intents= discord.Intents.default()
        intents.message_content = True #let em read the messages 
        super().__init__(command_prefix = "!", intents=intents, help_command=None) #Basically now creates a bot kind of like in the learning but now we subclassing

    async def on_ready(self):
        print("NatBot is ready to go!")

    async def setup_hook(self):
        await self.load_extension("identification") 

    async def on_guild_join(guild):
        # Try to find a suitable channel to send the message
        channel = guild.system_channel or next((c for c in guild.text_channels if c.permissions_for(guild.me).send_messages), None)

        if channel:
            await channel.send(f'Hello! I\'m {"☁️Nebula☁️"}, ready to help you identify clouds. Type !help to see my commands.')
        else:
            print(f"Could not send welcome msg in {guild.name}")



if __name__ == "__main__":
     
    load_dotenv()
    bot_key = os.getenv('bot_key')

    with open("whatis.json", 'r') as f:
        cloud_info = json.load(f)
    bot = NatBot()


 #or less of them i dont know what im doing :sob: 
    @bot.command()
    async def ping(ctx): #when user types prefix + fxn name (so in this case !ping). Also gives it the context which holds metadata
        await ctx.send("pong!")

    @bot.command()
    async def help(ctx):
        help_msg = '''
I'm Nebula, your local cloud-identifying bot!
-----------------
Right now, I can:

* Identify cloud types using !cloudId + image attachment 
    * When taking the photo, please make sure to get the cloud in the frame! Getting the ground is okay, too and can even be preferred (as some clouds are identified by heigh above ground)
* Give info on the cloud types with !info [cloudtype] command
* Tell you all of the cloudtypes with the !cloudnames command
        '''
        await ctx.send(help_msg)
    bot.run(bot_key)
