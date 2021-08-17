
from . import *
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from .utils import load_module
from .utils import start_assistant
from pathlib import Path
import asyncio
import telethon.utils



                    
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Speedo is checking")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print ('Lookup Completed And Initialzed')
    else:
        bot.start()


print("Loading Modules")
import glob
path = 'Speedo/plugins/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))   

import glob

path = 'Speedo/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Sucessfully Started Telethon Version Speedo Fastest bot")


print("Telethon All Configration Done checking that do you want Pyrogram Also or not")

op = os.environ.get("CLIENT", None)
if op == "Both":
  os.system("python3 -m main_start")
  print("Checking Sucess Pyrogram Will Too Load with telethon")
else:
  print("Checking Sucess Pyrogram Not Loading")
  pass


bot.loop.run_until_complete(op)
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
