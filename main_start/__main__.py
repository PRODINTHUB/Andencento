from session.pyrogram_main import *
from session.telethon import *
Session = os.environ.get("Client", None)
if Session == "Pyro" or "both":
  async def op():
    await mongo_check()
    await run_bot()
    Speedo.loop.run_until_complete(run_bot())
else:
  async def impro():
    print("Starting Telethon Since You have chosed Telethon")
