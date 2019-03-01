import discord
from discord.ext import commands
import youtube_dl
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


DEVELOPER_KEY = "AIzaSyC7Zxm1fWNZJOiw_CNIuB5s99x9DxKz0ao"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet",
    maxResults=max_results,
    location=location,
    locationRadius=location_radius

  ).execute()



  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result)
  try:
      nexttok = search_response["nextPageToken"]
      return(nexttok, videos)
  except Exception as e:
      nexttok = "last_page"
      return(nexttok, videos)


def geo_query(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'

    ).execute()

    return video_response








players = {}

class Voice:
  def __init__(self, client):
    self.client = client
    
  #Help voice
  async def on_message(self, message):
    if '.help all' in message.content or '.help voice' in message.content:
      embed=discord.Embed(title="Help - [Voice]", description="You must be in a voice channel to use these commands", color=0x0000ff)
      embed.add_field(name="--------------------", value="--------------------", inline=False)
      embed.add_field(name=".join", value="Join a voice channel", inline=False)
      embed.add_field(name=".leave", value="Leave a voice channel", inline=False)
      embed.add_field(name=".play [url]", value="Play audio from the youtube url", inline=False)
      embed.add_field(name=".pause", value="Pause current music", inline=False)
      embed.add_field(name=".resume", value="Resume current music", inline=False)
      embed.add_field(name=".stop", value="stop current music", inline=False)
      
      await self.client.send_message(message.channel, embed=embed)
    


    
    
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
    
    
  @commands.command(pass_context=True)
  async def youtube(self, ctx, arg):
    search = youtube_search(arg)
    await self.client.say(search)


def setup(client):
  client.add_cog(Voice(client))
