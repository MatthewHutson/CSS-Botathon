# -- Imports -- #
import json
import os
from user_class import User
from typing import Any
import discord

# -- Globals -- #
PATH: str = "save_data/"
EXTENSION: str = ".json"

# -- Functions -- #
def get_path(id: int) -> str: 
    global PATH, EXTENSION
    return PATH + str(id) + EXTENSION

def save_data(user: User) -> None:
    # -- Data Handling -- #
    data: dict[str, Any] = user.to_dict()

    # -- JSON Dumping -- #
    file_path: str = get_path(user.id)

    with open(file_path, "w") as file:
        json.dump(obj = data, fp = file)

def load_data(discord_user: discord.User) -> User:
    # -- Info -- #
    file_path: str = get_path(discord_user.id)

    if os.path.exists(file_path):
        # -- File Handling -- #
        with open(file_path, "r") as file:
            data: dict[str, Any] = json.load(fp = file)
            user = User(discord_user, **data)

    else: 
        # -- New User Case -- #
        user = User(discord_user)

    return user