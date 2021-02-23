# bot.py
import os
import discord
import requests
import json
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='meat', help='I\'ll reply with a nugget of wisdom.')
async def ron_swanson(ctx):
    response = requests.get(
        "http://ron-swanson-quotes.herokuapp.com/v2/quotes")
    json_data = json.dumps(response.json())
    quote = json_data.replace('[', '').replace(']', '').replace('"', '')
    await ctx.send(quote)

bot.run(TOKEN)
