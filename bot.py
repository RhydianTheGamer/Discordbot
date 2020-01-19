import discord
from discord.ext import commands
import time
import random
import asyncio
import os

PREFIX = '+'
client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
        activity = 'Hello there. Do +help for help'
        status = 'idle'
        print("Mother bot online")
        print()
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(activity))
        print("activity:",activity)
        print()
        print("status:",status)
client.run("NjY4MzUwMzg4OTgxOTg5Mzg2.XiQUUA.ei3ZK5KC6qG-kwr_Yosn3XhwHaA")
