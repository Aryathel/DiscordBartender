import discord
from discord.ext import commands

class General(commands.Cog, name = "General"):
    def __init__(self, bot):
        self.bot = bot
        print(f"Loaded General Cog.")

    def cog_unload(self):
        print(f"Unloaded General Cog.")

    @commands.command(name = "invite", help = "Get an invite link.")
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Invite Me To Your Server!",
            description = f"[Invite Link](https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=108608)",
            color = self.bot.color,
            url = f"https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=108608"
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(General(bot))
