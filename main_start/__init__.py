import os
Session = os.environ.get("Client", None)
if Session == "Tele":
  from session.telethon import *
  speedo = speedo
elif Session == "both":
  from session.pyrogram import *
  from session.telethon import *
  speedo = speedo
  client = Speedo
  friday_version = "0.1"
else:
  from session.pyrogram import *
client = Speedo
friday_version = "0.1"
