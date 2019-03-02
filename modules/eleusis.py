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
    if '.help all' in message.content or '.help eleusis' in message.content:
      embed=discord.Embed(title="Help - [Eleusis]", description="Commands about Eleusis", color=0x00ffff)
      embed.add_field(name="--------------------", value="--------------------", inline=False)
      embed.add_field(name=".eleusis rules", value="Give link to the game's rules", inline=False)
      
      await self.client.send_message(message.channel, embed=embed)
      
      
  #Commands
  @commands.command(pass_context=True)
  async def eleusis(self, ctx, *args):
      """Eleusis commands"""
      players = []
      
      class Game:
        def __init__(self):
         print('ok')
      
      
      if args[0] == 'rules':
        await self.client.say('http://laelith.fr/Zet/Articles/images/eleusis.pdf')
        
      elif args[0] == 'create':
        new_game_msg = await self.client.say("**A new game of Eleusis is being created ! React to join the party !**")
        
        end_msg = await self.client.wait_for_message(author=ctx.message.author, content=".eleusis start")
        new_game_msg = await self.client.get_message(ctx.message.channel, new_game_msg.id)

        for reaction in new_game_msg.reactions:
          await self.client.say(reaction.emoji)
          reactors = await self.client.get_reaction_users(reaction)
          for reactor in reactors:
            if reactor not in players:
              players.append(reactor)
          
        for player in players:
          await self.client.say(player.nick)


          
def setup(client):
  client.add_cog(Eleusis(client))
