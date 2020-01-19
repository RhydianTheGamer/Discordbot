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
#funcommands load
@client.command()
async def fcload(ctx, extension):
        client.load_extension(f'FunCommands.{extension}')


#funcommandsunload
@client.command()
async def fcunload(ctx, extension):
        client.unload_extension(f'FunCommands.{extension}')
for filename in os.listdir('./FunCommands'):
        if filename.endswith('.py'):
                client.load_extension(f'FunCommands.{filename[:-3]}')



#admincommands load
@client.command()
async def acload(ctx, extension):
        client.load_extension(f'AdminCommands.{extension}')


#admincommands unload
@client.command()
async def acunload(ctx, extension):
        client.unload_extension(f'AdminCommands.{extension}')

#admincommands
for filename in os.listdir('./AdminCommands'):
        if filename.endswith('.py'):
                client.load_extension(f'AdminCommands.{filename[:-3]}')

client.run("NjE5ODM0NTc2NjgzOTI1NTI0.XXX-xA.I3iYay81a2niHl-Cn7bOvK5D1SA")
