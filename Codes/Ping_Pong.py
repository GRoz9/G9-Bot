import discord
from discord.ext import commands

class PingPong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
      await ctx.send(f"Pong!\nBot latency = {round(self.bot.latency * 1000)}ms.")
      pass

def setup(bot):
    bot.add_cog(PingPong(bot))