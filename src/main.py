# -- Imports -- #
from __future__ import annotations
import discord
import os 
from dotenv import load_dotenv
from save_handler import *
from user_class import *
from prisoners import *

# -- Global Objects -- #
client = BotHandler()

# -- Adding Cogs -- #
client.add_cog(Dilemma())

# -- Events -- #
@client.event
async def on_ready() -> None:
    await client.get_log()
    loaded_message: str = f'{client.user} has connected to Discord!\n'
    await client.log(loaded_message)

#@client.slash_command(description='Start a Dilemma')
#async def dilemma(ctx: discord.ApplicationContext) -> None:
#    await ctx.respond('Here is a dropdown:', view=OptionView(), ephemeral=True)

# -- Main -- #
if __name__ == "__main__":
    load_dotenv()
    client.activate()
