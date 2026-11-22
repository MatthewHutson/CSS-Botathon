# -- Imports -- #
from __future__ import annotations
import discord
import os 
from dotenv import load_dotenv
import save_handler as save_handler
import user_class as user_class

# -- Classes -- #
class BotHandler(discord.Bot):
    # -- Attributes -- #
    log_channel: discord.abc.Guild | discord.Thread | discord.abc.PrivateChannel

    # -- Properties -- #
    @property
    def TOKEN(self) -> str: return os.getenv('TOKEN')

    @property
    def GUILD(self) -> str: return os.getenv('GUILD')

    @property
    def LOG(self) -> str: return os.getenv('LOG')

    # -- Methods -- #
    def __init__(self, *, loop = None, **options):
        # -- Intents -- #
        intents = discord.Intents()
        intents.polls = True
        intents.messages = True
        intents.guilds = True

        # -- Other -- #
        super().__init__(loop=loop, intents = intents, **options)

    def activate(self):
        self.run(self.TOKEN)

    async def get_log(self):
        channel = await self.fetch_channel(self.LOG)
        self.log_channel = channel

    async def log(self, message: str) -> None:
        print(self.log_channel)
        await self.log_channel.send(message)