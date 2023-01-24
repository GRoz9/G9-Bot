import discord,time
from discord.ext import commands

class Suggestion(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    @commands.command(name="suggest")
    async def suggest(self,ctx,*,Suggestion):
      await ctx.channel.purge(limit=1)
      await ctx.send("The Suggestion will be sent too: <#730547397884641311>")
      time.sleep(2)
      await ctx.channel.purge(limit=1)
      
      channel = discord.utils.get(ctx.guild.text_channels, name="🤷suggestions✅❌")
      
      #suggest = discord.Embed(title='New Suggestion!', description=f'{ctx.author.name} has suggested {Suggestion}.')
      suggest = discord.Embed(colour = 0x87CEEB)
      suggest.set_author(icon_url = f'{ctx.author.avatar_url}',name=f'Suggested by {ctx.message.author}' )
      suggest.add_field(name='New Suggestion!',value=f'{Suggestion}')
      
      sugg = await channel.send(embed=suggest)
      #await channel.send(f"^^ Suggestion ID: {sugg.id}")
      await sugg.add_reaction("✅")
      await sugg.add_reaction("❌")

      pass

def setup(bot):
    bot.add_cog(Suggestion(bot))