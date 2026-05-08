import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
import datetime
from zoneinfo import ZoneInfo

load_dotenv()

token = os.getenv("token")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=1388620030358589563))
    print(f"Bot {bot.user} is on...")

@bot.event
async def on_message(message):
    # if message.author.id == bot.user.id
    if message.author.bot:
        return
    else:
        if "god is good" in message.content.lower():
            await message.reply("Yes Amen 🙏 God is indeed good!")
        elif "revy" in message.content.lower():
            await message.reply("Revy is adorable :)")
        elif "pray for me" in message.content.lower():
            await message.reply(
        "🙏 We are praying for you!"
    )
        
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1388633482544283748)
    await channel.send(  f"""
✨ Welcome {member.mention} ✨

We are happy you joined Kingdom Connect 🙏
Please read the rules and enjoy the fellowship!
"""
)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1502239786277011466)
    await channel.send(f"""
 {member.mention} has left Kingdom Connect 💔
""")

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return
    channel = bot.get_channel(1502240853023002704)
    await channel.send(f"🗑️ Message deleted from {message.author.mention}\n"
        f"Content: {message.content}")

@bot.event
async def on_message_edit(before,after):
    if before.author.bot:
        return
    if before.content == after.content:
        return
    channel = bot.get_channel(1502239100504379416)
    
    await channel.send( f"✏️ {before.author.mention} edited a message.\n\n"
        f"Before: {before.content}\n"
        f"After: {after.content}")

@bot.command()
async def helpme(ctx):
    user = ctx.guild.get_member(1094655746928545914)
    await ctx.reply(f"{user.mention} help is needed here.")

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong! 🏓")

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

import datetime
from zoneinfo import ZoneInfo
import discord

@bot.tree.command(
    name="time",
    description="Get current time in major cities",
    guild=discord.Object(id=1388620030358589563)
)
async def get_time(interaction: discord.Interaction):

    now = datetime.datetime.now()

    times = {
        "🇮🇳 India (IST)": now.astimezone(ZoneInfo("Asia/Kolkata")),
        "🇺🇸 New York": now.astimezone(ZoneInfo("America/New_York")),
        "🇺🇸 Los Angeles": now.astimezone(ZoneInfo("America/Los_Angeles")),
        "🇬🇧 London": now.astimezone(ZoneInfo("Europe/London")),
        "🇫🇷 Paris": now.astimezone(ZoneInfo("Europe/Paris")),
        "🇦🇪 Dubai": now.astimezone(ZoneInfo("Asia/Dubai")),
        "🇯🇵 Tokyo": now.astimezone(ZoneInfo("Asia/Tokyo")),
        "🇦🇺 Sydney": now.astimezone(ZoneInfo("Australia/Sydney")),
    }

    msg = "🕒 **Current Time Around the World**\n\n"

    for city, t in times.items():
        msg += f"**{city}:** {t.strftime('%Y-%m-%d %H:%M:%S')}\n"

    await interaction.response.send_message(msg)

@bot.tree.command(name="greet",description="Greet the user with an optional message",guild=discord.Object(id=1388620030358589563))
async def greet(interaction:discord.Interaction,member:discord.Member,message:str|None=None):
    if message:
        await interaction.response.send_message(f"{message} {member.mention}")
    else:
        await interaction.response.send_message(f"Hello {member.mention}")

bot.run(token)




