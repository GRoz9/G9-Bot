import discord, os
from discord.ext import commands
from Other import Config

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            help_command=None,
            command_prefix=Config.prefix, 
            intents = discord.Intents.all(),
            client = commands.Bot(command_prefix="!", intents=discord.Intents.all()),
        )
      
        for filename in os.listdir("./Codes"):
            if filename.endswith(".py"):
              self.load_extension(f"Codes.{filename[:-3]}")
