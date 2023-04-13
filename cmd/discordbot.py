import discord
import discordmysql
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('discord bot starting')
  getUsersTerm()

@client.event
async def on_member_join(member):
  discordmysql.join_user(member)

def getUsersTerm():
  users = client.users
  for user in users:
    if user.bot == False:
      # client.user(user.id)
      print(user.name)

client.run(TOKEN)