import os
import datetime

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!', description = "Hero's Bartender", ignore_case = True)

bot.TOKEN = os.getenv('BartenderToken')
bot.log_channel_id = 601811847590576152
bot.color = discord.Color.from_rgb(250, 250, 250)

extensions = [
    'Cogs.bartender',
    'Cogs.listeners',
    'Cogs.general'
]

for extension in extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    game = discord.Game(name=f"Serving {len(bot.guilds)} guilds. | !help")
    await bot.change_presence(activity = game)

    embed = discord.Embed(
        title = "Bot Online!",
        color = bot.color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    channel = bot.get_channel(bot.log_channel_id)
    await channel.send(embed = embed)
    print(f"Connected to Discord with user {bot.user}! (ID: {bot.user.id})")

bot.run(bot.TOKEN, bot = True, reconnect = True)
