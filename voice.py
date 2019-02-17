import discord
from discord.ext import commands
import youtube_dl

players = {}

class Voice:
  def __init__(self, client):
    self.client = client
    
  #Help voice
  @commands.command(pass_context=True)
  async def help(self, ctx):
    if "all" or "voice" in ctx.message.content:
      embed=discord.Embed(title="Help - [Voice]", description="You must be in a voice channel to use these commands", color=0x0000ff)
      embed.add_field(name="--------------------", value="--------------------", inline=False)
      embed.add_field(name=".join", value="Join a voice channel", inline=False)
      embed.add_field(name=".leave", value="Leave a voice channel", inline=False)
      embed.add_field(name=".play [url]", value="Play audio from the youtube url", inline=False)
      embed.add_field(name=".pause", value="Pause current music", inline=False)
      embed.add_field(name=".resume", value="Resume current music", inline=False)
      embed.add_field(name=".stop", value="stop current music", inline=False)
      await self.client.say(embed=embed)
      
  #Voice commands
  
  @commands.command(pass_context=True)
  async def join(self, ctx):
    channel = ctx.message.author.voice.voice_channel
    await self.client.join_voice_channel(channel)
    await self.client.say(":microphone: Joined '{}' voice channel :microphone:".format(channel.name))

  @commands.command(pass_context=True)
  async def leave(self, ctx):
    channel = ctx.message.author.voice.voice_channel
    server = ctx.message.server
    voice_client = self.client.voice_client_in(server)
    await voice_client.disconnect()
    await self.client.say(":microphone: Left '{}' voice channel :microphone:".format(channel.name))
    
  @commands.command(pass_context=True)
  async def play(self, ctx, url):
    server = ctx.message.server
    voice_client = self.client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    await self.client.say(":musical_note: Now playing : {} :musical_note:".format(url))
    
  @commands.command(pass_context=True)
  async def pause(self, ctx):
    id = ctx.message.server.id
    players[id].pause()
    await self.client.say(":pause_button: Music paused :pause_button:")
    
  @commands.command(pass_context=True)
  async def resume(self, ctx):
    id = ctx.message.server.id
    players[id].resume()
    await self.client.say(":play_pause: Music resumed :play_pause:")
    
  @commands.command(pass_context=True)
  async def stop(self, ctx):
    id = ctx.message.server.id
    players[id].stop()
    await self.client.say(":stop_button: Music stopped :stop_button:")
    
    
def setup(client):
  client.add_cog(Voice(client))

