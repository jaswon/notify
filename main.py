from fbchat import Client
from fbchat.models import *
from bs4 import BeautifulSoup as Bs
from urllib.request import urlopen, Request

import creds

client = None

def selfMessage(m):
  if not client: client = Client(fb_email, fb_passw)
  client.sendMessage(
    m, 
    thread_id=client.uid, 
    thread_type=ThreadType.USER
  )

### check if PAX East Registration is open
def isOpen():
  headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',} 
  request = Request("http://east.paxsite.com/registration",None,headers)
  page = urlopen(request)
  soup = Bs(page, 'html.parser')
  return soup.body.contents[5].h2.strong.string != 'Registration opens soon'

print(isOpen())