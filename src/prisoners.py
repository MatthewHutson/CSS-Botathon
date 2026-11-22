import discord
from bot import *
from user_class import User
from save_handler import *

#    si   sp
# si 3/3  7/1
# sp 1/7  5/5

#    si   sp
# si 2/2  -2/4
# sp 4/-2  0/0

global ans, player1, player2, channel1, channel2, index
ans = ["", ""]
player1 = 0
player2 = 0
channel1 = 0
channel2 = 0
index = 0
total_players = 0
client = BotHandler()

class OptionSelect(discord.ui.Select):
    def __init__(self) -> None:
        options = [
            discord.SelectOption(label='Stay Silent'),
            discord.SelectOption(label='Snitch'),
        ]
        super().__init__(placeholder='Pick an Option', options=options)

    async def checkAns(self):
        global ans, player1, player2, index, total_players
        user_1 = load_data(player1._user)
        user_2 = load_data(player2._user)

        user_1.total_rounds += 1
        user_2.total_rounds += 1

        if index >= total_players:
            if ans[0] == ans[1]:
                if ans[0] == "Stay Silent":
                    await channel1.send("You both stayed silent\nYou both are locked up for 3 years (+2 points)")
                    await channel2.send("You both stayed silent\nYou both are locked up for 3 years (+2 points)")
                    user_1.total_score += 2
                    user_2.total_score += 2
                elif ans[0] == "Snitch":
                    await channel1.send("You both snitched\nYou both are locked up for 5 years (+0 points)")
                    await channel2.send("You both snitched\nYou both are locked up for 5 years (+0 points)")
                    user_1.total_score += 0
                    user_2.total_score += 0
                else:
                    raise Exception("INVALID CHOICES")
            else:
                if ans[0] == "Stay Silent":
                    await channel1.send("Your partner betrayed you\nYou both are locked up for 7 years (-2 points)")
                    await channel2.send("You betrayed your partner\nYou are locked up for 1 years (+4 points)")
                    user_1.total_score -= 2
                    user_2.total_score += 4
                elif ans[0] == "Snitch":
                    await channel1.send("You betrayed your partner\nYou are locked up for 1 years (+4 points")
                    await channel2.send("Your partner betrayed you\nYou both are locked up for 7 years (-2 points)")
                    user_1.total_score += 2
                    user_2.total_score -= 2
                else:
                    raise Exception("INVALID CHOICES")
            index = 0
            ans = ["", ""]
            total_players = 0

            save_data(user_1)
            save_data(user_2)

    async def callback(self, interaction: discord.Interaction) -> None:
        global ans, player1, player2, index, total_players
        await interaction.response.send_message(f'You picked {self.values[0]}!')
        if (index < total_players):
            ans[index] = self.values[0]
            index += 1
        await self.checkAns()

class OptionView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.add_item(OptionSelect())

class Dilemma(discord.Cog):
    @discord.Cog.listener()
    async def on_ready(self) -> None:
        print("Dilemma Cog is loaded")
    
    @discord.slash_command(description='Start a Dilemma')
    async def dilemma(self, ctx: discord.ApplicationContext, member: discord.Member) -> None:
        global player1, player2, channel1, channel2, total_players
        total_players += 2
        player1 = await ctx.author
        channel1 = await player1.create_dm()
        await channel1.send('Which will you pick:', view=OptionView())
        player2 = await member
        channel2 = await player2.create_dm()
        await channel2.send(f'{ctx.author._user.display_name} has challenged you\nWhich will you pick:', view=OptionView())