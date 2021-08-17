import os
Session = os.environ.get("Client", None)
if Session == "Tele":
  from session.telethon import *
else:
  from session.pyrogram import *
speedo = speedo
client = Speedo
friday_version = "0.1"
