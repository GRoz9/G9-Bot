import discord
from discord.ext import commands
from Other import Config

class MemberJoinLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.Cog.listener()
    async def on_member_join(self, member):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                if channel.id in Config.general_channel and channel in member.guild.text_channels:
                  embed = discord.Embed(
                    color=(discord.Color.from_rgb(0, 0, 128)),
                    title="Welcome To GHOST9!",
                    description="Hey,"
                    f"{member.mention}\n\n<@515660470217342977>&<@580106386571001868> are the owners and <@807618998874537984> is an Admin so if you need anything please do contact an <@&908849936139960381> or <@&585844054307110913> first. When you have settled please do add your Game, platform and region in <#646048574165090325> . Hopefully, You Enjoy Your Time Here!"
              )
                  await channel.send(embed=embed)
                    #await channel.send(f'Welcome to **{member.guild.name}**, {member.mention}, enjoy your stay!')
                    #return await member.add_roles(discord.utils.get(member.guild.roles, id=config.welcome_roles[member.guild.id]))
                    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                if channel.id in Config.staff_chat and channel in member.guild.text_channels:
                    return await channel.send(f"**{member}** has left! :sob:")
                    #return await channel.send(f'{member.mention} just left **{member.guild.name}**, what a shame.')

def setup(bot):
    bot.add_cog(MemberJoinLeave(bot))