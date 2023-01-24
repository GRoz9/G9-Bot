import discord
from discord.ext import commands
from discord import Embed, Emoji
from Other import Config

class ReactionRole(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, self.bot.guilds)
    if payload.message_id == 947159372100939866:
      member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
      emoji = payload.emoji.name
      if emoji == "Rocket_League":
        role = discord.utils.get(guild.roles, name="Rocket League")
      elif emoji == "Minectaft":
        role = discord.utils.get(guild.roles, name="Minecraft")
      elif emoji == "PC":
        role = discord.utils.get(guild.roles, name="PC")
      elif emoji == "PlayStation":
        role = discord.utils.get(guild.roles, name="PlayStation")
      elif emoji == "Xbox":
        role = discord.utils.get(guild.roles, name="Xbox")
      elif emoji == "NintendoSwitch":
        role = discord.utils.get(guild.roles, name="Nintendo Switch")
      elif emoji == "🇪🇺":
        role = discord.utils.get(guild.roles, name="EU")
      elif emoji == "🇺🇸":
        role = discord.utils.get(guild.roles, name="U.S")
      elif emoji == "OCE":
        role = discord.utils.get(guild.roles, name="OCE")
      elif emoji == "RL_Esports":
        role = discord.utils.get(guild.roles, name="TryOuts Rl")
      await member.add_roles(role)
    
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, self.bot.guilds)
    if payload.message_id == 947159372100939866:
      member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
      emoji = payload.emoji.name
      if emoji == "Rocket_League":
        role = discord.utils.get(guild.roles, name="Rocket League")
      elif emoji == "Minectaft":
        role = discord.utils.get(guild.roles, name="Minecraft")
      elif emoji == "PC":
        role = discord.utils.get(guild.roles, name="PC")
      elif emoji == "PlayStation":
        role = discord.utils.get(guild.roles, name="PlayStation")
      elif emoji == "Xbox":
        role = discord.utils.get(guild.roles, name="Xbox")
      elif emoji == "NintendoSwitch":
        role = discord.utils.get(guild.roles, name="Nintendo Switch")
      elif emoji == "🇪🇺":
        role = discord.utils.get(guild.roles, name="EU")
      elif emoji == "🇺🇸":
        role = discord.utils.get(guild.roles, name="U.S")
      elif emoji == "OCE":
        role = discord.utils.get(guild.roles, name="OCE")
      elif emoji == "RL_Esports":
        role = discord.utils.get(guild.roles, name="TryOuts Rl")
      await member.remove_roles(role)

  @commands.command()
  @commands.has_any_role("OWNERS OF GHOST9")
  async def react(self, ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("Here You Can Tell Us What Game You Play, On What Platform, On What Servers & If You Would Like to Join An Esports Team!")
    Reaction = discord.Embed(title = "Games, Platform, Region & Esports", description = "Please Add One Of Each At Least!", colour = 0x00008B)
    Reaction.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", value="Games:\n" f"{Config.Rl} \n {Config.Minecraft}", inline=False)
    Reaction.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", value="Platform:\n" f"{Config.PC} \n {Config.PS} \n {Config.Xbox} \n {Config.Switch}", inline=False)
    Reaction.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", value="Region:\n" f"{Config.EU} \n {Config.US} \n {Config.OCE}", inline=False)
    Reaction.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", value="If you would like to try out:\n" f"{Config.Esports}", inline=False)
    react_messasge = await ctx.send(embed=Reaction)
    
    await react_messasge.add_reaction(Config.Rl)
    await react_messasge.add_reaction(Config.Minecraft)
    await react_messasge.add_reaction(Config.PC)
    await react_messasge.add_reaction(Config.PS)
    await react_messasge.add_reaction(Config.Xbox)
    await react_messasge.add_reaction(Config.Switch)
    await react_messasge.add_reaction(emoji = "🇪🇺")
    await react_messasge.add_reaction(emoji = "🇺🇸")
    await react_messasge.add_reaction(Config.OCE)
    await react_messasge.add_reaction(Config.Esports)
    #sugg = await channel.send(embed=suggest)
    #await channel.send(f"^^ Suggestion ID: {sugg.id}")
    pass

def setup(bot):
  bot.add_cog(ReactionRole(bot))