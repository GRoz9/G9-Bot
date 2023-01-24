import discord, os
from discord.ext import commands
from discord import Member
from pymongo import MongoClient
from typing import Optional
from Other import Config

 
DataBaseG9 = os.environ["DataBaseG9"]
cluster = MongoClient("mongodb+srv://GRoz9:GRozanski942005@gr9.6uqcu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#cluster = MongoClient("mongodb+srv://<GRoz9>:<GRozanski942005>@<GHOST9>/<Levelling System>?ssl=true&ssl_cert_reqs=CERT_NONE")
levelling = cluster["GHOST9"]["LevellingSystem"]

class LevellingSys(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_message(self, message):
    #if message.channel.ID in Config.XP_C:
    stats = levelling.find_one({"ID" : message.author.id})
    if not message.author.bot:
      if stats is None:
        newuser = {"Name": message.author.name, "ID" : message.author.id, "XP": 50}
        levelling .insert_one(newuser)
      else:
        # A = 5*(N^2 + 8*N + 11)
        XP = stats["XP"] + 5
        levelling.update_one({"ID" : message.author.id}, {"$set" : {"XP": XP, "Name": message.author.name}})
        lvl = 0
        while True:
          if XP < ((50*(lvl**2))+(50*lvl)):
            break
          lvl += 1
        XP -= ((50*((lvl-1)**2))+(50*(lvl-1)))
        if XP == 0:
          channel = self.bot.get_channel(636399538650742795)
          await message.channel.send(f"Well done {message.author.mention}! You leveled up to **level: {lvl}**!")
          for i in range(len(Config.Leveled_Roles)):
            if lvl == levelnum[i]:
              await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=Config.Leveled_Roles[i]))
              embed = dsicord.Embed(description=f"{message.author.mention} you have gotten role **{Config.Leveled_Roles[i]}**!")
              embed.set_thumbnail(url=message.author.avatar_url)
              await message.channel.send(embed=embed)

  @commands.command(name = "Rank", aliases=["rank", "level"])
  async def Rank(self, ctx, target: Optional[Member]):
    target = target or ctx.author
    
    stats = levelling.find_one({"ID" : target.id})
    if stats is None:
      embed = discord.Embed(description="Haven't received a rank yet, time to start typing!")
      await ctx.channel.send(embed=embed)
    else:
      XP = stats["XP"]
      lvl = 0
      rank = 0
      while True:
        if XP < ((50*(lvl**2))+(50*lvl)):
          break
        lvl += 1
      XP -= ((50*((lvl-1)**2))+(50*(lvl-1)))
      boxes = int((XP/(200*((1/2) * lvl)))*20)
      ranking = levelling.find().sort("XP",-1)
      for x in ranking:
        rank += 1
        if stats["ID"] == x["ID"]:
          break
      embed = discord.Embed(title="{}'s level stats".format(target.name))
      embed.add_field(name="Name", value=target.mention, inline=True)
      embed.add_field(name='Level', value=f"{lvl}", inline=True)
      embed.add_field(name="XP", value=f"{XP}/{int(200*((1/2)*lvl))}", inline=True)
      embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
      embed.add_field(name="Progress Bar [lvl]", value=boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline=False)
      embed.set_thumbnail(url=target.avatar_url)
      await ctx.channel.send(embed=embed)

  @commands.command(name = "Top", aliases=["top"])
  async def LeaderBoard(self,ctx):
    rankings = levelling.find().sort("XP",-1)
    i = 1
    embed = discord.Embed(title="Rankings:")
    for x in rankings:
      try:
        temp = ctx.guild.get_member(x["ID"])
        tempxp = x["XP"]
        embed.add_field(name=f"{i}: {temp.name}",value=f"Total XP: {tempxp}", inline=False)
        i += 1
      except:
        pass
      if i == 11:
        break
    await ctx.channel.send(embed=embed)
  pass
    


def setup(bot):
  bot.add_cog(LevellingSys(bot))