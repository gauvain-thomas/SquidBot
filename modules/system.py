#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import subprocess

owners = ['263670024391229440']

class System:
  def __init__(self, client):
    self.client = client

  @commands.command(pass_context=True)
  async def reboot(self, ctx):
      """Reboot client"""
      if ctx.message.author.id in owners:
          await self.client.say("Reboot in process...")
          print("Reboot in process")
          subprocess.call("../start.sh", shell=True)
          sys.exit()
      else:
          await self.client.say("Access denied")

  @commands.command(pass_context=True)
  async def shutdown(self, ctx):
      """Turn client off"""
      if ctx.message.author.id in owners:
          await self.client.say("Turning off...")
          print("Turning off...")
          sys.exit()
      else:
          await self.client.say("Access denied")

def setup(client):
  client.add_cog(System(client))
