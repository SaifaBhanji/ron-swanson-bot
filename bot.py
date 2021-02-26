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
RURU_ID = os.getenv('RURU_ID')
SAIFA_ID = os.getenv('SAIFA_ID')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."))


@bot.command(name='meat', help='I\'ll reply with a nugget of wisdom.')
async def ron_swanson(ctx):
    response = requests.get(
        "http://ron-swanson-quotes.herokuapp.com/v2/quotes")
    json_data = json.dumps(response.json())
    quote = json_data[2:-2]
    await ctx.send(quote)


@bot.command(name='define', help='You turned me into a dictionary?!', pass_context=True)
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


@bot.command(name='boop', help='You guys are gross.', pass_context=True)
async def ron_swanson(ctx, *, person):

    if len(person.split()) > 1:
        await ctx.send("Hold on! I can only boop one person at a time!")

    if (person.lower() == 'ruru'):
        user = await bot.fetch_user(RURU_ID)
        await user.send("Saifa is booping you!")
        await ctx.send("I booped her.")
    elif (person.lower() == 'saifa'):
        user = await bot.fetch_user(SAIFA_ID)
        await user.send("Ruru is booping you!")
        await ctx.send("I booped him.")
    else:
        await ctx.send("Sorry, I can't boop that person.")

bot.run(TOKEN)
