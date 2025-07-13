import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="testing.env")

bot_key = os.getenv('bot_key')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_read():
    print(f'hi {client.user} is here!')

client.run(bot_key)

