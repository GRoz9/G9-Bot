import discord
from discord.ext import commands

class example(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def example(self, message):
    # empty for future features to be added
    pass

def setup(bot):
  bot.add_cog(example(bot))