from session.pyrogram_main import *
Session = os.environ.get("Client", None)
if Session == "Pyro":
  async def op():
    await mongo_check()
    await run_bot()
    Speedo.loop.run_until_complete(run_bot())
elif Session == "both":
  async def impro(): 
    from session.telethon_main import *
    await mongo_check()
    await run_bot()
    Speedo.loop.run_until_complete(run_bot())
    speedo.loop.run_until_complete(run_bot())
    print("Starting Telethon && pyrogram")
else:
  async def imoort():
    from session.telethon_main import *
    await speedo.start()
