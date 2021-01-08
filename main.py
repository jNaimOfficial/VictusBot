import discord
from discord.ext import commands
import json


CONFIG = json.load(open("CONFIG.json"))
BOT_TOKEN = json.load(open("BOT_TOKEN.json"))

bot = commands.Bot(command_prefix= CONFIG["PREFIX"])

@bot.event
async def on_ready():
    pass
bot.run(BOT_TOKEN["TOKEN"])
