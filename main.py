import discord
import asyncio
import aiohttp
import datetime
from bs4 import BeautifulSoup as Bs

import creds
client = discord.Client()
recipient = discord.Object(id=creds.recipient)

### check if PAX East Registration is open
async def status():
  try:
    async with aiohttp.get("http://east.paxsite.com/registration") as r:
      if r.status == 200:
        soup = Bs(await r.text(), 'html.parser')
        banner = soup.select(".message h2 strong")
        if len(banner) and banner[0].text == "Registration opens soon":
          return None
        else:
          return "Website changed"
  except e:
    return "Website error"

# check every 30 seconds, notify if true
async def todo():
  await client.wait_until_ready()
  while not client.is_closed:
    check = await status()
    if check is not None:
      await client.send_message(recipient,check)
    else:
      print('[{:%Y-%m-%d %H:%M:%S}] - no change'.format(datetime.datetime.now()))
    await asyncio.sleep(30)

@client.event
async def on_ready():
  await client.send_message(recipient, "notify_me started")

client.loop.create_task(todo())
client.run(creds.token)
