import discord
from bot import *

#    si   sp
# si 3/3  7/1
# sp 1/7  5/5

#    si   sp
# si 2/2  -2/4
# sp 4/-2  0/0

client = BotHandler()

class OptionSelect(discord.ui.Select):
    def __init__(self) -> None:
        options = [
            discord.SelectOption(label='Stay Silent'),
            discord.SelectOption(label='Snitch'),
        ]
        super().__init__(placeholder='Pick an Option', options=options)

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f'You picked {self.values[0]}!')

class OptionView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.add_item(OptionSelect())

class Dilemma(discord.Cog):
    @discord.Cog.listener()
    async def on_ready(self) -> None:
        print("Dilemma Cog is loaded")
    
    @discord.slash_command(description='Start a Dilemma')
    async def dilemma(self, ctx: discord.ApplicationContext) -> None:
        await ctx.respond('Here is a dropdown:', view=OptionView(), ephemeral=True)