#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import subprocess
import sys

owners = ['263670024391229440']

class System:
  def __init__(self, client):
    self.client = client

  #Help system
  async def on_message(self, message):
    if '.help all' in message.content or '.help system' in message.content:
      embed=discord.Embed(title="Help - [System]", description="Only authorized members can use these commands", color=0xff0000)
      embed.add_field(name="--------------------", value="--------------------", inline=False)
      embed.add_field(name=".reboot", value="Restart bot and update code from github", inline=False)
      embed.add_field(name=".shutdown", value="Turn bot off", inline=False)
      
      await self.client.send_message(message.channel, embed=embed)
      
  #Commands
  @commands.command(pass_context=True)
  async def reboot(self, ctx):
      """Reboot bot"""
      if ctx.message.author.id in owners:
        await self.client.say("Reboot in process...")
        print("Reboot in process")
        source = os.path.dirname(__file__)
        parent = os.path.join(source, '../')
        script_path = os.path.join(parent, 'start.sh')
        subprocess.call(script_path, shell=True)
        sys.exit()
      else:
          await self.client.say("Access denied")

  @commands.command(pass_context=True)
  async def shutdown(self, ctx):
      """Turn bot off"""
      if ctx.message.author.id in owners:
          await self.client.say("Turning off...")
          print("Turning off...")
          sys.exit()
      else:
          await self.client.say("Access denied")

def setup(client):
  client.add_cog(System(client))
