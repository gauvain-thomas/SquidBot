#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import os
import subprocess
import sys
import random

owners = ['263670024391229440']


# Game class
class Game:
    cards = [
    '1_Clubs', '2_Clubs', '3_Clubs', '4_Clubs', '5_Clubs', '6_Clubs', '7_Clubs', '8_Clubs', '9_Clubs', '10_Clubs', 'J_Clubs', 'Q_Clubs', 'K_Clubs',
    '1_Diamonds', '2_Diamonds', '3_Diamonds', '4_Diamonds', '5_Diamonds', '6_Diamonds', '7_Diamonds', '8_Diamonds', '9_Diamonds', '10_Diamonds', 'J_Diamonds', 'Q_Diamonds', 'K_Diamonds',
    '1_Hearts', '2_Hearts', '3_Hearts', '4_Hearts', '5_Hearts', '6_Hearts', '7_Hearts', '8_Hearts', '9_Hearts', '10_Hearts', 'J_Hearts', 'Q_Hearts', 'K_Hearts',
    '1_Spades', '2_Spades', '3_Spades', '4_Spades', '5_Spades', '6_Spades', '7_Spades', '8_Spades', '9_Spades', '10_Spades', 'J_Spades', 'Q_Spades', 'K_Spades'
    ]

    def __init__(self, client, channel, players):
        self.client = client
        self.channel = channel
        self.players = players
        self.decks = {}

    async def start(self):
        await self.client.send_message(self.channel, 'Game is about to start ! Players are :')
        for player in self.players:
            print(player.name)
            deck = []
            # await self.client.send_message(self.channel, player.name)
            await self.client.send_message(player, 'Good luck !')
            for i in range(14):
                deck.append(random.choice(Game.cards))
            self.decks[player.id] = deck
            await self.client.send_message(player, decks[player.id])

class Eleusis:
  def __init__(self, client):
    self.client = client

  #Help system
  async def on_message(self, message):
    if '.help all' in message.content or '.help eleusis' in message.content:
      embed=discord.Embed(title="Help - [Eleusis]", description="Commands about Eleusis", color=0x00ffff)
      embed.add_field(name="--------------------", value="--------------------", inline=False)
      embed.add_field(name=".eleusis rules", value="Give link to the game's rules", inline=False)
      embed.add_field(name=".eleusis create", value="Create a new party, waiting for playing to react until game is started", inline=False)
      embed.add_field(name=".eleusis start", value="Launch a new game, must be used after creating a new party", inline=False)
      await self.client.send_message(message.channel, embed=embed)


  #Commands
  @commands.command(pass_context=True)
  async def eleusis(self, ctx, *args):
      """Eleusis commands"""

      if args[0] == 'rules':
        await self.client.say('http://laelith.fr/Zet/Articles/images/eleusis.pdf')




#       New Game
      elif args[0] == 'create':
        players = []

        new_game_msg = await self.client.say("**A new game of Eleusis is being created ! React to join the party !**")

        end_msg = await self.client.wait_for_message(author=ctx.message.author, content=".eleusis start")
        new_game_msg = await self.client.get_message(ctx.message.channel, new_game_msg.id)

        for reaction in new_game_msg.reactions:
          reactors = await self.client.get_reaction_users(reaction)
          for reactor in reactors:
            # if reactor not in players:
            players.append(reactor)

        new_game = Game(self.client, ctx.message.channel, players)
        await new_game.start()


def setup(client):
  client.add_cog(Eleusis(client))
