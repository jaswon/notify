import discord
import asyncio
from bs4 import BeautifulSoup as Bs
from urllib.request import urlopen, Request

import creds
client = discord.Client()
chan = discord.Object(id=creds.server)

### check if PAX East Registration is open
headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',} 
request = Request("http://east.paxsite.com/registration",None,headers)
def isOpen():
  soup = Bs(urlopen(request), 'html.parser')
  return soup.body.contents[5].h2.strong.string != 'Registration opens soon'

async def todo():
  await client.wait_until_ready()
  while not client.is_closed:
    if isOpen():
      await client.send_message(channel, "REGISTRATION OPEN GOGOGOGO")
    await asyncio.sleep(30) # task runs every 60 seconds

@client.event
async def on_ready():
  await client.send_message(chan, "notify_me started")

client.loop.create_task(todo())
client.run(creds.token)