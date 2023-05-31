import os
import json
import platform
import discord
from discord.ext import commands

with open("config.json", "r") as file:
    config = json.load(file)
TEST_GUILD = discord.Object(id=config["test-guild"])


class BotTemplate(commands.Bot):
    async def setup_hook(self):
        for cog_file in os.listdir("./cogs"):
            if cog_file.endswith(".py"):
                await self.load_extension(f"cogs.{cog_file[:-3]}")
        self.tree.copy_global_to(guild=TEST_GUILD)
        await self.tree.sync(guild=TEST_GUILD)


intents = discord.Intents.default()
intents.message_content = True
client = BotTemplate(intents=intents, command_prefix=config["prefix"]["std"])


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    home_channel = client.get_channel(config["bot-testing"])
    await home_channel.send(f"Running on ``{platform.system()}`` as ``{client.user}`` with ID ``{client.user.id}``.")

client.run(config["token"])
