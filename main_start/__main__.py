from session.pyrogram_main import *
if Session == "Pyro" or "Both":
  async def op():
    await mongo_check()
    await run_bot()
    Speedo.loop.run_until_complete(run_bot())
else:
  return
