from datetime import datetime
from typing import Optional

import discord,time,asyncio
from discord.ext import commands
from discord import Embed, Member
from discord.ext.commands import command,Cog
from asyncio import sleep


class MemberCount(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_member_join(self,member):
    test = self.bot.get_channel(934571328843960360)
    await sleep(10*5)
    for channel in member.guild.channels:
      if channel.name.startswith("👫 Members:"):
        with open("Other/Goal.txt", "r") as f:
          global Goal
          Goal = int(f.read())
        if len(list(filter(lambda m: not m.bot, member.guild.members))) == Goal:
          print("test")
          await test.send(f"@everyone We had finally reached our goal of **50 Members!** and thank you everyone for being apart of this :tada: :tada: :tada: and thanks to our {Goal}'th member **{member.mention}!**")
        await channel.edit(name=f"👫 Members: {len(list(filter(lambda m: not m.bot, member.guild.members)))}")
      elif channel.name.startswith("🤖 Bots:"):
        await channel.edit(name=f"🤖 Bots: {len(list(filter(lambda m: m.bot, member.guild.members)))}")      
        break

  @commands.Cog.listener()
  async def on_member_remove(self,member):
    await sleep(10*5)
    for channel in member.guild.channels:
      if channel.name.startswith("👫 Members:"):
        await channel.edit(name=f"👫 Members: {len(list(filter(lambda m: not m.bot, member.guild.members)))}")
      elif channel.name.startswith("🤖 Bots:"):
        await channel.edit(name=f"🤖 Bots: {len(list(filter(lambda m: m.bot, member.guild.members)))}")      
        break

  @commands.command(name="MemberGoal", aliases=["membergoal", "MG", "mg"])
  @commands.has_any_role("OWNERS OF GHOST9")
  async def MemberGoal(self, ctx):
    print("Tets")
    await ctx.channel.send("**G, You Will Have 10 Seconds 2 Answer NGL!**")
    await ctx.channel.send("**Whats The Goal This Time Big Man?**")
    try:
      print("test 1")
      global MGoal
      MGoal = await self.bot.wait_for("message",check=lambda message: message.author == ctx.author and message.channel == ctx.channel,timeout = 10.0)
      print("Test 2")
      with open("Other/Goal.txt", "w") as f:
        #f.write(f"Goal: {MGoal.content}")   
        f.write(f"{MGoal.content}")   
        f.close()
      if MGoal:
        print("test 5")
        channel = self.bot.get_channel(949649906912600104)
        await channel.edit(name=f"🥅 Current goal: {MGoal.content}")
    except asyncio.TimeoutError:
      await ctx.channel.send("**Big Man, You Took TOOOO Long, Hurry The F Up Next Time!**")
    pass

def setup(bot):
  bot.add_cog(MemberCount(bot))