from telethon import TelegramClient

import os
import sys
from telethon.sessions import StringSession
from telethon import SpeedoClient


tele-session = os.environ.get("TELETHON_SESSION", None)
ap = os.environ.get("API_ID", None)
API = os.environ.get("API_HASH", None)
if tele-session:
    session_name = str(tele-session)
    speedo = SpeedoClient(StringSession(session_name), ap, API)
else:
    session_name = "startup"
    speedo = SpeedoClient(session_name, ap, API)


CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

