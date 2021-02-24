# bot.py
import os
import discord
import requests
import json
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DICTIONARY_API_ID = os.getenv('DICTIONARY_API_ID')
DICTIONARY_API_KEY = os.getenv('DICTIONARY_API_KEY')

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


@bot.command(name='define', help='You turned me into a dictionary??', pass_context=True)
async def ron_swanson(ctx, *, word):

    if len(word.split()) > 1:
        await ctx.send("Hold on! Only one word at a time!")

    else:
        url = "https://od-api.oxforddictionaries.com/api/v2/entries/en-us/" + word.lower()

        response = requests.get(
            url, headers={"app_id": DICTIONARY_API_ID, "app_key": DICTIONARY_API_KEY})
        response = response.json()
        definition = response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]

        await ctx.send(word + " : " + definition)

bot.run(TOKEN)
