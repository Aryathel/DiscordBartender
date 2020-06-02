import random
import asyncio

import discord
from discord.ext import commands

class Bartender(commands.Cog, name = 'Bartender'):
    def __init__(self, bot):
        self.bot = bot
        print("Loaded Bartender Cog.")

    def cog_unload(self):
        print(f"Unloaded Bartender Cog.")

    @commands.command(name = 'coffee', help = "Order a cup of coffee.")
    async def get_coffee(self, ctx):
        await self.get_item(ctx, 'coffee', '☕')

    @commands.command(name = 'beer', help = "Order a beer.")
    async def get_beer(self, ctx):
        await self.get_item(ctx, 'beer', '🍺')

    @commands.command(name = 'whisky', help = "Order a whisky.")
    async def get_whisky(self, ctx):
        await self.get_item(ctx, 'whisky', '🥃')

    @commands.command(name = 'manhattan', help = "Order a manhattan.")
    async def get_manhattan(self, ctx):
        await self.get_item(ctx, 'manhattan', '🍸')

    @commands.command(name = 'martini', help = "Order a martini.")
    async def get_martini(self, ctx):
        await self.get_item(ctx, 'martini', '🍸')

    @commands.command(name = 'margarita', help = "Order a margarita.")
    async def get_margarita(self, ctx):
        await self.get_item(ctx, 'margarita', '🍸')

    @commands.command(name = 'mojito', help = "Order a mojito.")
    async def get_mojito(self, ctx):
        await self.get_item(ctx, 'mojito', '🍸')

    @commands.command(name = 'bloody-mary', aliases=['bloodymary', 'bloody_mary', 'bm'], help = "Order a bloody mary.")
    async def get_bm(self, ctx):
        await self.get_item(ctx, 'bloody mary', '🍸', image='bm')

    @commands.command(name = 'mai-tai', aliases=['maitai', 'mai_tai', 'mt'], help = "Order a mai tai.")
    async def get_mt(self, ctx):
        await self.get_item(ctx, 'mai tai', '🥃', image='tm')

    @commands.command(name = 'tequila', help = "Order a tequila.")
    async def get_tequila(self, ctx):
        await self.get_item(ctx, 'tequila', '🥃')

    @commands.command(name = 'vodka', help = "Order a vodka.")
    async def get_vodka(self, ctx):
        await self.get_item(ctx, 'vodka', '🥃')

    @commands.command(name = 'old-fashioned', aliases=['oldfashioned', 'old_fashioned', 'of'], help = "Order an old fashioned.")
    async def get_of(self, ctx):
        await self.get_item(ctx, 'old fashioned', '🥃', image='of')

    @commands.command(name = 'chips', help = "Order chips.")
    async def get_chips(self, ctx):
        await self.get_item(ctx, 'chips', '🍿')

    @commands.command(name = 'breadsticks', aliases = ['bs'], help = "Order breadsticks.")
    async def get_bs(self, ctx):
        await self.get_item(ctx, 'breadsticks', '🍿', image = 'bs')

    @commands.command(name = 'crackers', help = "Order crackers.")
    async def get_crackers(self, ctx):
        await self.get_item(ctx, 'crackers', '🍿')

    @commands.command(name = 'peanuts', help = "Order peanuts.")
    async def get_peanuts(self, ctx):
        await self.get_item(ctx, 'peanuts', '🥜')

    @commands.command(name = 'popcorn', help = "Order popcorn.")
    async def get_popcorn(self, ctx):
        await self.get_item(ctx, 'popcorn', '🍿')

    @commands.command(name = 'rum', help = "Order rum.")
    async def get_rum(self, ctx):
        await self.get_item(ctx, 'rum', '🥃')

    async def get_item(self, ctx, type, emoji, image = None):
        await ctx.trigger_typing()
        if not image:
            image = type
        num = random.randint(1, 5)
        file = discord.File(f"./images/{image}{num}.jpg", filename = f"{image}.jpg")
        embed = discord.Embed(
            title = f"Please wait while I prepare your {type}...",
            color = self.bot.color
        )
        message = await ctx.send(embed = embed)
        await ctx.trigger_typing()
        await asyncio.sleep(5)
        embed = discord.Embed(
            title = f"Here is your {type}, sir. {emoji}",
            color = self.bot.color
        )
        embed.set_image(url=f"attachment://{image}.jpg")
        await message.delete()
        message = await ctx.send(embed = embed, file = file)
        for reaction in ['👍', '👎']:
            await message.add_reaction(reaction)

def setup(bot):
    bot.add_cog(Bartender(bot))
