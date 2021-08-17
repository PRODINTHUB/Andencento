from session.pyrogram_main import *
Session = os.environ.get("Client", None)
if Session == "Pyro":
  async def op():
    await mongo_check()
    await run_bot()
    Speedo.loop.run_until_complete(run_bot())
else:
  await mongo_check()
