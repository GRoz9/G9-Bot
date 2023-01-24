import os
from Other.webserver import keep_alive
from Other.GHOST9 import Bot

def main():
  bot = Bot()
  TOKEN = os.environ.get("TOKEN")
  keep_alive()
  try:
    bot.run(TOKEN)
  except:
    os.system("kill 1")

if __name__=="__main__":
  main()


# import asyncio, os, discord
# from discord.ext import commands

# intents = discord.Intents.all()
# client = commands.Bot(command_prefix="!", intents=intents, help_command=None)
# TOKEN = os.environ.get("TOKEN")

# async def load():
#   for filename in os.listdir("./Codes"):
#     if filename.endswith(".py"):
#         client.load_extension(f"Codes.{filename[:-3]}")

# async def main():
#   await load()
#   await client.start(TOKEN)

# asyncio.run(main())