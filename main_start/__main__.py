from session.pyrogram_main import *
from session.telethon import *
Session = os.environ.get("Client", None)
if Session == "Pyro":
  async def op():
    await mongo_check()
    await run_bot()
    Speedo.loop.run_until_complete(run_bot())
elif Session == "Pyro":
  async def impro():
    await mongo_check()
    await run_bot()
    print("Starting Telethon && pyrogram")
else:
  async def imoort()
