# -- Imports -- #
import save_handler
from main import BotHandler
import discord
from dotenv import load_dotenv
import user_class

# -- Globals -- #
test_client2 = BotHandler()

# -- Tests -- #
async def test() -> None:
    id = 711599047672332289
    discord_user: discord.User = await test_client2.fetch_user(id)
    user: user_class.User = save_handler.load_data(discord_user)

    print(user.total_score)

    user.total_rounds += 2
    user.total_score += 3

    print(user.total_score)

    save_handler.save_data(user)

    user.total_rounds += 2
    user.total_score += 3

    print(user.total_score)

    user = save_handler.load_data(discord_user)

    print(user.total_score)

# -- Events -- #
@test_client2.event
async def on_ready() -> None:
    await test_client2.get_log()
    loaded_message: str = f'{test_client2.user} has connected to Discord For Testing the loading functions!\n'
    await test_client2.log(loaded_message)
    await test()

# -- Main -- #
if __name__ == "__main__":
    load_dotenv()
    test_client2.activate()