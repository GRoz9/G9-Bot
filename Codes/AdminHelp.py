import discord
from discord.ext import commands

class AdminHelp(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name="Ahelp", aliases=["ahelp", "AHelp"])
  @commands.has_any_role("OWNERS OF GHOST9", "ADMIN", "MODERATORS")
  async def Ahelp(self, ctx, user: discord.Member=None):
    
      if user==None:
        user=ctx.author
  
      rlist = []
      for role in user.roles:
        if role.name != "@everyone":
          rlist.append(role.mention)
  
      print(rlist)
      em = discord.Embed(title="Help For Higher Roles", description="Prefix = ! (Under Construction)",colour=user.color) 
      em.add_field(name="Temporary", value="Bla Bla")
      em.add_field(name="Temporary", value="Bla Bla")
      em.add_field(name="Temporary", value="Bla Bla")
      await ctx.send(embed = em)


def setup(bot):
  bot.add_cog(AdminHelp(bot))