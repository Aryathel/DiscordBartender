import discord
from discord.ext import commands

class Listeners(commands.Cog, name = "Listeners"):
    def __init__(self, bot):
        self.bot = bot
        print("Loaded Listeners Cog.")

    def cog_unload(self):
        print(f"Unloaded Listeners Cog.")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        game = discord.Game(name=f"Serving {len(self.bot.guilds)} guilds. | !help")
        await self.bot.change_presence(activity = game)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        game = discord.Game(name=f"Serving {len(self.bot.guilds)} guilds. | !help")
        await self.bot.change_presence(activity = game)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if len(message.mentions) > 0 and message.mentions[0].id == self.bot.user.id:
                await message.channel.send("How can I help you?")

def setup(bot):
    bot.add_cog(Listeners(bot))
