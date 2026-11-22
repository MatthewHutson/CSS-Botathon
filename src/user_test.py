# -- Imports -- #
import user_class
from bot import BotHandler
import discord
from dotenv import load_dotenv

# -- Globals -- #
test_client = BotHandler()

# -- Tests -- #
async def test() -> None:
    id = 711599047672332289
    discord_user = await test_client.fetch_user(id)
    user = user_class.User(discord_user)

    print(user.total_score, user.total_rounds)

    user.total_rounds += 2
    user.total_score += 3

    print(user.average_score)

# -- Events -- #
@test_client.event
async def on_ready() -> None:
    await test_client.get_log()
    loaded_message: str = f'{test_client.user} has connected to Discord For Testing the User Class!\n'
    await test_client.log(loaded_message)
    await test()

# -- Main -- #
if __name__ == "__main__":
    load_dotenv()
    test_client.activate()