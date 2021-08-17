
import glob
import os
from pathlib import Path

from telethon.tl.functions.channels import JoinChannelRequest



from .telethon import *
from .client.telethon.utils import *
from .client.telethon.config import Config

hl = Config.HANDLER
PIC = Config.ALIVE_PIC or "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
ALIVE = Config.YOUR_NAME or "ANDENCENTO USER"
Andencento_mention = f"[{ALIVE}]"
user_mention = Andencento_mention
ver = "0.0.2"


async def asst():
  """
  Loading Assistant From here
  """
  path = 'assistant/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      start_assistant(shortname.replace(".py", ""))

async def plugs():
  """
  Modules From here
  """
  path = "plugins/*.py"
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))


async def addons():
  extra_repo = "https://github.com/Andencento/Addons-Andencento"
  if Config.EXTRA == "True":
    try:
      os.system(f"git clone {extra_repo}")  
    except BaseException:
      pass
    LOGS.info("Installing Extra Plugins")
    path = "Addons-Andencento/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as ex:
        path2 = Path(ex.name)
        shortname = path2.stem
        extra(shortname.replace(".py", ""))


async def op():
    await Andencento(JoinChannelRequest("Andencento"))
    await Andencento(JoinChannelRequest("AndencentoSupport"))

