import discord
from discord.ext import commands

class MusicHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="MusicHelp", aliases=["musichelp", "Musichelp"])
    async def MusicHelp(self, ctx, user:discord.Member=None):
      
      if user==None:
        user=ctx.author

      rlist = []
      for role in user.roles:
        if role.name != "@everyone":
          rlist.append(role.mention)

      print(rlist)
      em = discord.Embed(title="Music Commands", description="Prefix = !",colour=discord.Color.from_rgb(255,105,180))
      em.add_field(name="Join", value="Join the vc that the current user is in", inline=False)
      em.add_field(name="Leave", value="Leave the vc that the current user is in", inline=False)
      em.add_field(name="Play", value="Play a song, given either a url or a search term", inline=False)
      em.add_field(name="Pause", value="Pauses current song", inline=False)
      #em.add_field(name="Loop", value = "Loops through the current or next song until disabled.")
      em.add_field(name="Skip", value="Skips current song", inline=False)
      em.add_field(name="Stop", value="Stops playing and clears queue", inline=False)
      em.add_field(name="ClearQueue", value="Clears the queue", inline=False)
      em.add_field(name="Queue", value="Shows the queue", inline=False)
      await ctx.send(embed = em)
      pass

def setup(bot):
    bot.add_cog(MusicHelp(bot))