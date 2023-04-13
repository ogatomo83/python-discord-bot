import discord
import discord-mysql
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
  discord-mysql.join_user(member)

def getUsersTerm():
  users = client.users
  for user in users:
    if user.bot == False:
      # client.user(user.id)
      print(user.id)

client.run(TOKEN)