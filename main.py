import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import randint, choice

from modules.channel_redirect import ChannelRedirect

load_dotenv()

intents = discord.Intents().default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    channel_dict = {
            "cpp": "#Pretend that this is a cpp channel",
            "c++": "#Pretend that this is a cpp channel",
            "python": "#Pretend that this is a python channel",
    }

    redirector = ChannelRedirect(channel_dict, message.content)
    relevant_channels = redirector.get_relevant_channel()
    redirect_message = f"For more information consult these channels:\n{
            "\n".join(relevant_channels)
    }"

    await message.channel.send(redirect_message)

    await bot.process_commands(message)

@bot.command(name="say", help="Make the bot say something")
async def say(ctx, *, arg):
    await ctx.send(arg)

@bot.command(name="roll", help="Roll an n sided dice.")
async def roll(ctx, faces: int) -> None:
    await ctx.send(f"The dice says {randint(1, faces)}")

@bot.command(name="ping_random", help="Pings a random person")
async def ping_random_copy(ctx):
    member_list = ctx.guild.members
    random_user = choice(member_list)

    await ctx.send(random_user.mention)

def main():
    token = os.getenv('TOKEN')
    bot.run(token)

if __name__ == "__main__":
    main()

