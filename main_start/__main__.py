from session.pyrogram_main import *
Session = os.environ.get("Client", None)
if Session == "Pyro":
  async def op():
    await mongo_check()
    await run_bot()
    Speedo.loop.run_until_complete(run_bot())
elif Session == "both":
  
  print("Starting Telethon && pyrogram")
  from session.telethon_main import *
  async def op():
    await mongo_check()
    await run_bot()
    Speedo.loop.run_until_complete(run_bot())
    speedo.loop.run_until_complete(run_bot())
else:
  from session.telethon_main import *
  await speedo.start()
