#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import os
import subprocess
import sys

owners = ['263670024391229440']

class Eleusis:
  def __init__(self, client):
    self.client = client

  #Help system
  async def on_message(self, message):
    if '.help all' in message.content or '.help eulesis' in message.content:
      embed=discord.Embed(title="Help - [Eleusis]", description=" - ", color=0x00ffff)
      embed.add_field(name="--------------------", value="--------------------", inline=False)
      embed.add_field(name=".eleusis rules", value="Give link to the game's rules", inline=False)
      
      await self.client.send_message(message.channel, embed=embed)
      
  #Commands
  @commands.command(pass_context=True)
  async def eleusis(self, ctx, args*):
      """Eleusis commands"""
      if args[0] == 'rules':
        await self.clinet.say('http://laelith.fr/Zet/Articles/images/eleusis.pdf')

          
def setup(client):
  client.add_cog(System(client))
