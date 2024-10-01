import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import randint

load_dotenv()

intents = discord.Intents().default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

ping = False
ping_interval = int()

@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")

@bot.event
async def ping_random(ctx) -> None:
    mention_list = list()
    for guild in bot.guilds:
        for member in guild.members:
            mention_list.append(member.mention)

    i = randint(0, len(mention_list)-1)
    await ctx.send(mention_list[i])

@bot.command(name="say", help="Make the bot say something")
async def say(ctx, *, arg):
    await ctx.send(arg)

@bot.command(name="roll", help="Roll an n sided dice.")
async def roll(ctx, faces: int) -> None:
    await ctx.send(f"The dice says {randint(1, faces)}")

@bot.command(name="ping_random", help="Pings a random person")
async def ping_random_copy(ctx):
    await ping_random(ctx)

@bot.command(name="ping_random_every", help="Ping a random person every 10 seconds.")
async def ping_random_every(ctx, will_ping: str) -> None:
    global ping 
    if will_ping in ["true", "True"]:
        ping = True
    else:
        ping = False

def main():
    token = os.getenv('TOKEN')
    bot.run(token)

if __name__ == "__main__":
    main()

