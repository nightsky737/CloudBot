import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
 
load_dotenv()
bot_key = os.getenv('bot_key')
my_guild_name = os.getenv('my_server_name')

class NatBot(commands.Bot):
    def __init__(self):
        intents= discord.Intents.default()
        intents.message_content = True #let em read the messages 
        super().__init__(command_prefix = "!", intents=intents) #Basically now creates a bot kind of like in the learning but now we subclassing
        self.add_command(self.ping)

    #No more wrappers!
    async def on_read(self):
        print("NatBot is ready to go!")


if __name__ == "__main__":
    bot = NatBot()
    bot.load_extension('identification')
 #or less of them i dont know what im doing :sob: 
    @bot.command()
    async def ping(ctx): #when user types prefix + fxn name (so in this case !ping). Also gives it the context which holds metadata
        await ctx.send("pong!")

  
    @bot.command()
    async def help(ctx):
        help_msg = '''
        Hi! I'm Nat, short for NatBot! You can give me pictures of clouds, (maybe rocks if I get around to that) or wildlife that I will identify!
        Type !cloud or !animal or !plant, attach your images, and send!
        '''
        await ctx.send(help_msg)

        
    bot.run(bot_key)

 