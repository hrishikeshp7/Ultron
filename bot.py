import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="u!")

@client.command()
async def load(self,ctx):
	client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(self,ctx):
	client.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')


client.run('Token here')