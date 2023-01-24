import discord, time
from discord.ext import commands
from Other import Config

class Report(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name = "report", aliases=["Report"])
  async def report(self, ctx, member:discord.Member, *, report=None):
    time.sleep(3)
    await ctx.channel.purge(limit=1)
    if ctx.channel.id == 947458514320785459:
      Report_Channel = discord.utils.get(ctx.guild.channels, name = "report⚠")
      if member is None:
        return await ctx.send("Please inclue a user!")
      if report is None:
        return await ctx.send("Please inclue information!")
      else:
        Report = discord.Embed(title="Report", description=f"{ctx.author.mention} has reported {member}", colour=discord.Color.from_rgb(150,0,0))
        #Report.set_author(url = "")
        Report.add_field(name = "More Info:", value = f"{report}")
        Report.set_footer(icon_url = ctx.author.avatar_url, text = f"React with the ✅ if the situation has been delt with!")
        report_message = await Report_Channel.send(embed=Report)
        await report_message.add_reaction("✅")
        await ctx.send(f"{ctx.author.mention} Your report has been sent to the staff team!")
        time.sleep(10)
        await ctx.channel.purge(limit=1)
  
        try:
          def check(reaction, user):
            #return user == ctx.author and str(reaction.emoji) in ["✅"]
            return str(reaction.emoji) in ["✅"] 
          reaction, user = await self.bot.wait_for("reaction_add", timeout=604800, check=check)
          if str(reaction.emoji) == "✅":
            await Report_Channel.purge(limit=1)
            await ctx.author.send("Your report has been looked into and delt with,\nThank you for reporting! 🙂")
  
        except Execption as e:
          print(e)
    else:
      await ctx.send(f"{ctx.author.mention} Please Use <#947458514320785459> to send a report!")
    pass  
  

def setup(bot):
    bot.add_cog(Report(bot))