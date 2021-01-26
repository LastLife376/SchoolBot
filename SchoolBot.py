import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''


bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Hello!')


bot.run('ODAzNjUwMTE5MDkwMDQ0OTc4.YBA3fw.3oVtmqvvP-MhcOrtxySXPmfJEEA')
