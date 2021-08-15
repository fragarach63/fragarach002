import asyncio
from asyncio.tasks import ALL_COMPLETED
import discord
from discord.ext import commands
import json
import random
import os, asyncio

intents = discord.Intents.default()
intents.members = True


with open('Setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='$', intents = intents)

@bot.event
async def on_ready():
   print(">>Bot is online<<")

#@bot.command()
#async def 圖片(ctx):
   #pic = discord.File('pic')
   #await ctx.send(file= pic)

@bot.command()
async def load(ctx, extension):
   bot.load_extension(f'cmds.{extension}')
   await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
   bot.unload_extension(f'cmds.{extension}')
   await ctx.send(f'UN-Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
   bot.reload_extension(f'cmds.{extension}')
   await ctx.send(f'RE-Loaded {extension} done.')

for filename in os.listdir('./cmds'):
   if filename.endswith('.py'):
      bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
   bot.run(jdata['TOKEN'])   

