from discord.ext import commands, tasks
import discord
import json
from discord import Embed
import asyncio


client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="currently being worked on"))
    print(f'{client.user} is ready!')


client.run('ODAzNjUwMTE5MDkwMDQ0OTc4.YBA3fw.OZDwB6yddq0xEejS6fRj0INwFZk')
