#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import os
import subprocess
import sys

owners = ['263670024391229440']

class System:
  def __init__(self, client):
    self.client = client

  #Help system
  async def on_message(self, message):
    if '.help all' in message.content or '.help modules' in message.content:
      embed=discord.Embed(title="Help - [Modules]", description="Only authorized members can use these commands", color=0xff0000)
      embed.add_field(name="--------------------", value="--------------------", inline=False)
      embed.add_field(name=".reboot", value="Restart bot and update code from github", inline=False)
      embed.add_field(name=".shutdown", value="Turn bot off", inline=False)
      
      await self.client.send_message(message.channel, embed=embed)
    
      
  #Commands
  @commands.command(pass_context=True)
  async def modules(self, ctx, arg):
      """Modules"""
      if ctx.message.author.id in owners:
        if arg == 'reboot':
          print('Reboot modules')
          await self.cient.say('Reboot modules')
          source = os.path.dirname(__file__)
          parent = os.path.join(source, '../')
          script_path = os.path.join(parent, 'modules.sh')
          subprocess.call(script_path, shell=True)
          sys.exit()
      else:
          await self.client.say("Access denied")


def setup(client):
  client.add_cog(System(client))
