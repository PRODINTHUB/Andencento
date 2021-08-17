from telethon import TelegramClient

import os
import sys
from telethon.sessions import StringSession
from telethon import SpeedoClient

Session = os.environ.get("Client", None)
tele_session = os.environ.get("TELETHON_SESSION", None)
ap = os.environ.get("API_ID", None)
API = os.environ.get("API_HASH", None)
if Session == "Tele" or "both":
    try:
        if tele_session:
            session_name = str(tele_session)
            speedo = SpeedoClient(StringSession(session_name), ap, API)
        else:
            session_name = "startup"
            speedo = SpeedoClient(session_name, ap, API)
    except Exception:
        speedo = None

CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

