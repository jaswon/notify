import discord
import asyncio
import aiohttp
import datetime
from bs4 import BeautifulSoup as Bs

import creds
client = discord.Client()
recipient = discord.Object(id=creds.recipient)

### check if PAX East Registration is open
async def isOpen():
  async with aiohttp.get("http://east.paxsite.com/registration") as r:
    if r.status == 200:
      res = await r.text()
      soup = Bs(res, 'html.parser')
      return soup.body.contents[5].h2.strong.string != 'Registration opens soon'
  return false

# check every 30 seconds, notify if true
async def todo():
  await client.wait_until_ready()
  while not client.is_closed:
    if await isOpen():
      await client.send_message(recipient, "REGISTRATION OPEN GOGOGOGO")
    else:
      print('[{:%Y-%m-%d %H:%M:%S}] - no change'.format(datetime.datetime.now()))
    await asyncio.sleep(30)

@client.event
async def on_ready():
  await client.send_message(recipient, "notify_me started")

client.loop.create_task(todo())
client.run(creds.token)
