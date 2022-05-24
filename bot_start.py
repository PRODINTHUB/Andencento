import os
import sys
choice = os.environ.get("CLIENT")

if choice == "pyrogram" or "Pyrogram" or "PYROGRAM":
   os.system("python -m main_start")
elif choice == "Telethon" or "telethon" or "TELETHON":
  os.system("python -m Speedo")
elif choice == "both" or "Both" or "BOTH":
  os.system("python -m main_start && python -m Speedo")
else:
  sys.exit()
