import os
from discord.ext import commands

bot = commands.Bot(command_prefix="")


@bot.event
async def on_ready():
    print("Bot Ready.")


@bot.event
async def on_message(message):
    if message.content == ">ping":
        await message.channel.send("Pong.")

print("xxx")
print(os.environ.get("token", "uu"))

bot.run(os.environ.get("token", "xx"))
