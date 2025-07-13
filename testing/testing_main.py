import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

#Use dotenv file so that we dont put secret keys in github.
load_dotenv(dotenv_path="testing.env")
bot_key = os.getenv('bot_key')
my_guild_name = os.getenv('my_server_name')
#Intents is where you tell the bot what u wanna do with it.
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#Client.event is a wrapper fxn that links the fxn u define to the event
#Event is smth in discord that code listens for and responds to
#Alternatively we could subclass client and override the on_ready method of client.
@client.event
async def on_ready():
    #On ready runs when you connect to it
    print(f'{client.user} is ready to go!')

    #Apparently discord servers are called guilds. Anyways  discord.find is p useful
    #Basically runs until that lambda fxn is true searching the iterable in second args position
    #That lambda fxn is called a predicate to identify the element we're tryna find
    guild = discord.utils.find(lambda guild: guild.name == my_guild_name, client.guilds)
    
    #Or alternatively get:
    guild = discord.utils.get(client.guilds, name=my_guild_name)
    print(f'Ready to go be useuful in {guild.name} with id {guild.id}')

#Passes in the message as message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Sends it in the same channel message was sent from
    await message.channel.send("great message! This def wont get annoying fast!")

client.run(bot_key)
