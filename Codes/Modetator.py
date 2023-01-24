import discord, datetime, aiofiles, os, pymongo
from discord.ext import commands
from pymongo import MongoClient
#from Other.Config import Pag

DataBaseG9 = os.environ["DataBaseG9"]
cluster = MongoClient("mongodb+srv://GRoz9:GRozanski942005@gr9.6uqcu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
Warning = cluster["GHOST9"]["Moderation"]

class Modetator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

###----------------------------Kick/Ban Command!----------------------------###
  
    @commands.command(name="kick")
    @commands.has_any_role("OWNERS OF GHOST9")
    async def kick(self, ctx, user : discord.Member = None, *, reason = None):
        if user is None:
            em = discord.Embed(title="**Please specify a user to kick.**", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)

        if user.id == ctx.author.id:
            em = discord.Embed(title="**You cannot kick yourself.**", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)

        if user.top_role >= ctx.author.top_role:
            em = discord.Embed(title=f"{user.name} could not be kicked, they have higher or equal roles to you.", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)

        try:
            await user.kick(reason=str(reason))
        except discord.errors.Forbidden:
            em = discord.Embed(title=f"{user.name} could not be kicked.", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)


        # for user
        userEmbed = discord.Embed(title=f"You have been kicked from {ctx.guild.name}", colour=discord.Color.purple())
        userEmbed.add_field(name="Reason", value=str(reason))
        userEmbed.add_field(name="Date", value=str(datetime.datetime.now()))
        try:
            await user.send(embed=userEmbed)
        except Exception:
            pass

        # for channel
        channelEmbed = discord.Embed(title=f"{user.display_name} has been kicked from {ctx.guild.name}", colour=discord.Color.purple())
        channelEmbed.add_field(name="Reason", value=str(reason))
        channelEmbed.add_field(name="Date", value=str(datetime.datetime.now()))
        await ctx.send(embed=channelEmbed)

    @commands.command(name="ban",help="Ban a given user with a given reason")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user : discord.Member = None, *, reason = None):
        if user is None:
            em = discord.Embed(title="**Please specify a user to ban.**", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)

        if user.id == ctx.author.id:
            em = discord.Embed(title="**You cannot ban yourself.**", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)

        if user.top_role >= ctx.author.top_role:
            em = discord.Embed(title=f"{user.name} could not be banned, they have higher or equal roles to you.", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)

        try:
            await user.ban(reason=str(reason))
        except discord.errors.Forbidden:
            em = discord.Embed(title=f"{user.name} could not be banned.", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)


        # for user
        userEmbed = discord.Embed(title=f"You have been banned from {ctx.guild.name}", colour=discord.Color.purple())
        userEmbed.add_field(name="Reason", value=str(reason))
        userEmbed.add_field(name="Date", value=str(datetime.datetime.now()))
        try:
            await user.send(embed=userEmbed)
        except Exception:
            pass

        # for channel
        channelEmbed = discord.Embed(title=f"{user.display_name} has been banned from {ctx.guild.name}", colour=discord.Color.purple())
        channelEmbed.add_field(name="Reason", value=str(reason))
        channelEmbed.add_field(name="Date", value=str(datetime.datetime.now()))
        await ctx.send(embed=channelEmbed)

    @commands.command(name="unban",help="Unbans a given user followed by their discriminator")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member = None):

        if member is None:
            em =  discord.Embed(title="**Please enter a user's ID or name followed by their discriminator.**", colour=discord.Color.purple())
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)

        member_name, member_discriminator = member.split("#")

        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:
            user = ban_entry.user

            if (member_name, member_discriminator) == (user.name, user.discriminator):
                await ctx.guild.unban(user)
                em =  discord.Embed(title=f"Unbanned {user.name}", colour=discord.Color.purple())
                em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                return await ctx.send(embed=em)
        em =  discord.Embed(title="**The given user either doesn't exist or is not banned.**", colour=discord.Color.purple())
        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        return await ctx.send(embed=em)


###----------------------------Warn Command!----------------------------###
  
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role("OWNERS OF GHOST9")
    async def warn(self, ctx, member: discord.Member, *, reason):
      print("test ")
      if member.id in [ctx.author.id, self.bot.user.id]:
        return await ctx.send("You cannot warn yourself or the bot!")
      print("Test ")
      current_warn_count = len(
          await self.bot.warns.find_many_by_custom(
              {
                  "user_id": member.id,
                  "guild_id": member.guild.id
              }
          )
      ) + 1
      print("Test 2") 
      warn_filter = {"user_id": member.id, "guild_id": member.guild.id, "number": current_warn_count}
      warn_data = {"reason": reason, "timestamp": ctx.message.created_at, "warned_by": ctx.author.id}
      
      await self.bot.warns.upsert_custom(warn_filter, warn_data)
      
      embed = discord.Embed(
          title="You are being warned:",
          description=f"__**Reason**__:\n{reason}",
          colour=discord.Colour.red(),
          timestamp=ctx.message.created_at
      )
      embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
      embed.set_footer(text=f"Warn: {current_warn_count}")
      
      try:
          await member.send(embed=embed)
          await ctx.send("Warned that user in dm's for you.")
      except discord.HTTPException:
          await ctx.send(member.mention, embed=embed)
            
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role("OWNERS OF GHOST9")
    async def warns(self, ctx, member: discord.Member):
      warn_filter = {"user_id": member.id, "guild_id": member.guild.id}
      warns = await self.bot.warns.find_many_by_custom(warn_filter)
      
      if not bool(warns):
          return await ctx.send(f"Couldn't find any warns for: `{member.display_name}`")
      
      warns = sorted(warns, key=lambda x: x["number"])
      
      pages = []
      for warn in warns:
          description = f"""
          Warn Number: `{warn['number']}`
          Warn Reason: `{warn['reason']}`
          Warned By: <@{warn['warned_by']}>
          Warn Date: {warn['timestamp'].strftime("%I:%M %p %B %d, %Y")}
          """
          pages.append(description)
      
      await Pag(
          title=f"Warns for `{member.display_name}`",
          colour=0xCE2029,
          entries=pages,
          length=1
      ).start(ctx)

    @commands.command(aliases=["delwarn", "dw"])
    @commands.has_any_role("OWNERS OF GHOST9")
    @commands.guild_only()
    async def deletewarn(self, ctx, member: discord.Member, warn: int = None):
      """Delete a warn / all warns from a given member"""
      filter_dict = {"user_id": member.id, "guild_id": member.guild.id}
      if warn:
          filter_dict["number"] = warn

      was_deleted = await self.bot.warns.delete_by_custom(filter_dict)
      if was_deleted and was_deleted.acknowledged:
          if warn:
              return await ctx.send(
                  f"I deleted warn number `{warn}` for `{member.display_name}`"
              )

          return await ctx.send(
              f"I deleted `{was_deleted.deleted_count}` warns for `{member.display_name}`"
          )

      await ctx.send(
          f"I could not find any warns for `{member.display_name}` to delete matching your input"
      )

def setup(bot):
    bot.add_cog(Modetator(bot))