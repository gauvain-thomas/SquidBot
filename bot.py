#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import subprocess
import os
import sys

file=open('home/pi/Bot/token.txt', 'r')
TOKEN = file.read().rstrip("\n")

description = '''SquidBot in Python'''
bot_prefix = (".",";",":","!")
bot = commands.Bot(command_prefix=bot_prefix, description=description)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print("ID : " + bot.user.id)
    print("Token : " + TOKEN)
    print('------')
    print('Servers connected to:')
    for server in bot.servers:
        print(server.name)
    print('------')
    await bot.change_presence(game=discord.Game(name='humans...', type=3))
    
@bot.event
async def on_member_join(member):
    await bot.send_message(member.server, "Hello")

    
#Commands

@bot.command()
async def help():
    help=discord.Embed(title="Help", description="List of all commands", color=0x00ff00)
    help.set_author(name="SquidBot")
    help.add_field(name=".help", value="Shows this message", inline=False)
    help.set_footer(text="SquidBot, the best half-squid half-robot bot.")
    await bot.say(embed=help)
    
@bot.command(pass_context=True)
async def reboot(ctx):
    """Reboot bot"""
    if ctx.message.author.id == '263670024391229440':
        await bot.say("Reboot in process...")
        print("Reboot in process")
        subprocess.call("./start.sh", shell=True)
        sys.exit()
    else:
        await bot.say("Access denied")
     
@bot.command(pass_context=True)
async def stop(ctx):
    """Turn bot off"""
    if ctx.message.author.id == '263670024391229440':
        await bot.say("Turning off...")
        print("Turning off...")
        sys.exit()
    else:
        await bot.say("Access denied")
     
@bot.command()
async def hello():
    """Says world"""
    await bot.say("world !")
    
@bot.command()
async def github():
    """Give github's link"""
    await bot.say("https://github.com/Squidoss/SquidBot")
    

bot.run(TOKEN)
