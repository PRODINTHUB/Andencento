from .__main__ import Session
if Session == "Tele":
  from session.telethon import *
else:
  from session.pyrogram import *
speedo = speedo
client = Speedo
friday_version = "0.1"
