#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'cards_img'))
print(sys.path)
import display_cards

owners = ['263670024391229440']


# Game class
class Game:
    """Eleusis game class"""

    class Player():
        """Eleusis game player sub-class"""
        def __init__(self, client, player):
            self.client = client
            self.player = player
            self.deck = []
            self.score = 0
            self.player_status = 'player'

        def create_deck(self):
            self.deck = []
            for i in range(14):
                self.deck.append(random.choice(Game.cards))

        def set_player_status(self, status):
            self.player_status = status

        def is_god(self):
            if self.player_status == 'god':
                return True
            else:
                return False

        async def show_deck(self):
            await self.client.send_message(self.player, 'Your deck : {}'.format(self.deck))

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
        self.players_obj = {}

        #Set players object
        for player in self.players:
            self.players_obj[player.id] = Game.Player(self.client, player)

    async def start(self):
        self.turn = 1

        self.up_row = [(0, '')]
        self.middle_row = [(0, '')]
        self.down_row = [(0, '')]

        await self.show_scores()
        self.pick_god()
        self.reset_decks()

        self.middle_row.append((self.turn, random.choice(Game.cards)))

        await self.show_cards()
        await self.show_decks()

        await self.process_turn()

    def reset_decks(self):
        for player in self.players:
            if not self.players_obj[player.id].is_god():
                self.players_obj[player.id].create_deck()

    def pick_god(self):
        self.god = random.choice(self.players)
        self.players_obj[self.god.id].set_player_status('god')

    async def show_cards(self):
        display_cards.create_image(self.up_row, self.middle_row, self.down_row)
        await self.client.send_file(self.channel, r"/home/pi/Bot/SquidBot/modules/cards_img/temp.png",filename="Cards.png",content='Cards')
        await self.client.send_message(self.channel, 'Cards are : {}'.format(self.middle_row))
        await self.client.send_message(self.channel, 'Rejected cards are : {}'.format(self.down_row))

    async def show_decks(self):
        for player in self.players:
            if not self.players_obj[player.id].is_god():
                await self.players_obj[player.id].show_deck()

    async def show_scores(self):
        embed=discord.Embed(title="[Eleusis]", description="Scores", color=0x00ffff)

        for player in self.players:
            embed.add_field(name=player.name, value=self.players_obj[player.id].score, inline=False)

        await self.client.send_message(self.channel, embed=embed)

    async def process_turn(self):
        for player in self.players:
            if not self.players_obj[player.id].is_god():
                chosen_card = ''
                while not chosen_card in self.cards and chosen_card in self.players_obj[player.id].deck:
                    await self.client.send_message(player, 'Choose a card.. .')
                    chosen_msg = await self.client.wait_for_message(author=player)
                    chosen_card = chosen_card_msg.content
                    if not chosen_card in self.cards:
                        await self.client.send_message(player, "This card doesn't exist, please try again")
                    elif not chosen_card in self.players_obj[player.id].deck:
                        await self.client.send_message(player, "This card is not in your deck, please try again")

                # self.players_obj[player.id].deck.remove(chosen_card)
                await self.players_obj[player.id].show_deck()

                await self.client.send_message(player, 'Card chosen')
                await self.client.send_message(self.god, 'Does this card fit the sequence ? (yes, no): {}'.format(chosen_card))
                answer = await self.client.wait_for_message(author=self.god)
                answer_message = ''

                while not (answer_message == 'yes' or answer_message == 'no'):
                    answer_message = answer.content
                    print('Wait for answer ' + answer_message)
                    if answer_message == 'yes':
                        self.turn += 1
                        self.middle_row.append((self.turn, chosen_card))
                    elif answer_message == 'no':
                        self.down_row.append((self.turn, chosen_card))
                    else:
                        await self.client.send_message(self.god,
                        'Sorry, your message was not fully understood, please try again')
                        answer = await self.client.wait_for_message(author=self.god)

                await self.show_cards()

                if len(self.players_obj[player.id].deck) == 0:
                    await self.client.send_message(self.chanel, '{} has won !'.format(player.name))
                    self.satrt()

        await self.process_turn()



class Eleusis:
  def __init__(self, client):
    self.client = client
    self.games_list = {}
  #Help Eleusis
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
            if reactor not in players:
                players.append(reactor)

        if len(players) > 1:
            self.games_list[ctx.message.channel.id] = Game(self.client, ctx.message.channel, players)
            await self.games_list[ctx.message.channel.id].start()
        else:
            await self.client.say('Not enough players, start again')

def setup(client):
  client.add_cog(Eleusis(client))
