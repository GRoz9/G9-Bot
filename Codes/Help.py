import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["Help"])
    async def help(self, ctx):
        em = discord.Embed(title="Help", description="Prefix = !",color=(discord.Color.from_rgb(0, 0, 128))) #colour=discord.Color.purple())
        # em.add_field(name="Ban", value="Bans a user")
        # em.add_field(name="Kick", value="Kicks a user")
        # em.add_field(name="Unban", value="Unbans a user")
        # em.add_field(name="Clear", value="Clears the channel by either a certain number of messages, or left blank, the whole channel")
        em.add_field(name="MusicHelp", value="Shows commands for the music options!")
        em.add_field(name="Ahelp", value="Shows commands for moderators and above!") 
        em.add_field(name="ForzaRandom", value="Randomises set of challanges whilst building your car!")
        em.add_field(name="whois", value="Information about a set discord account in G9!")
        em.add_field(name="ping", value="Latency of the bot!")
        em.add_field(name="Suggest", value="Allows you to send a suggestion!")
        em.add_field(name="Report", value="Report a user and a reason for to the staff team. Use <#947458514320785459>")
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Help(bot))