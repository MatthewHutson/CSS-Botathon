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

@client.slash_command(description='Get Your Average Score Per Game')
async def get_score(ctx: discord.ApplicationContext) -> None:
    discord_user = ctx.author
    user: User = load_data(discord_user)
    await ctx.respond(f'Your average score per game is {user.average_score}!')

# -- Main -- #
if __name__ == "__main__":
    load_dotenv()
    client.activate()
