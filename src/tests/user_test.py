# -- Imports -- #
from backend.user_class import *
from bot.main import BotHandler

# -- Globals -- #
test_client = BotHandler()

# -- Events -- #
@test_client.event
async def on_ready() -> None:
    await test_client.get_log()
    loaded_message: str = f'{test_client.user} has connected to Discord For Testing the User Class!\n'
    await test_client.log(loaded_message)

# -- Main -- #
if __name__ == "__main__":
    test_client.activate()