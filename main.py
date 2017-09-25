from fbchat import Client
from fbchat.models import *

from creds import *

client = Client(fb_email, fb_passw)

def selfMessage(m):
  client.sendMessage(
    m, 
    thread_id=client.uid, 
    thread_type=ThreadType.USER
  )

selfMessage("hello me")