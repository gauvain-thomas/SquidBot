import discord
from discord.ext import commands
import subprocess

TOKEN = 'NTM2OTY3NzEyMTExNTkxNDMz.Dzykmw.J1nBswy-HqDTBu9yafoOUdAo_MU'

description = '''SquidBot in Python'''
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print("ID : " + bot.user.id)
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world !")
    
    
@bot.command()
async def reboot(pass_context=True):
    """Reboot bot"""
    if ctx.author.id == '263670024391229440':
        await bot.say("Redémarrage en cours")
        print("Redémarrage en cours")
        subprocess.call("./start.sh", shell=True)
    else:
        await bot.say("Vous n'avez pas les droits")
        

bot.run(TOKEN)
