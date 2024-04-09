import discord
import os
import requests
import json
from random import randrange
import feedparser
from keep_alive import keep_alive


my_secret = os.environ['TOKEN']
client = discord.Client()
a = []

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0] ['q'] + " -" + json_data[0] ['a']
  return(quote)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Technical issues'))  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith('hello'):
    await message.channel.send('Hello!')

  elif message.content.startswith('gm'):
    await message.channel.send('Good Morning!')

  elif message.content.startswith('no u'):
    await message.channel.send('poda nee')

  elif message.content.startswith('shut up'):
    await message.channel.send('no u')   

  elif message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)     

  elif message.content.startswith('$news'):
    url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
    f=feedparser.parse(url)
    for entry in f.entries:
      a.append(entry.title)
    newsHeadlines = '\n\n'.join((line) for line in a)
    await message.channel.send(newsHeadlines + "\nSource:- Times of India")  

  elif message.content.startswith('$8ball'):
    b=randrange(0,2)
    if (b==0):
      c='Yes'
    else:
      c='No'
    await message.channel.send(c)  

keep_alive()    
client.run(os.getenv('TOKEN'))
