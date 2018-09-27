import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print("The bot is online!")
    
lines = open(r'Minecraft.txt').read().splitlines()

@bot.command(pass_context=True)
async def minecraft (ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Minecraft Account", color=0x00ff40)
    embed.set_thumbnail(url="https://pre00.deviantart.net/2640/th/pre/f/2016/133/0/d/minecraft_hd_logo_by_nuryrush-da2aumi.png")
    embed.add_field(name="Account details:", value=split[0], inline=True)
    embed.set_footer(text="Made by iBoy21™#8792")
    await bot.send_message(ctx.message.author, embed=embed)

bot.run('NDk0OTA2MjI4OTk3MjI2NTA4.Do6Vmg.dx7VtZgpGdugLIXIhyYgI93U6QI')
