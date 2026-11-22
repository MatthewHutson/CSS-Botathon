# -- Imports -- #
from dataclasses import dataclass
from typing import Any
import discord

# -- Classes -- #
class User():
    # -- Attributes -- #
    discord_user: discord.User
    total_score: int
    total_rounds: int

    # -- Properties -- #
    @property
    def average_score(self) -> float: 
        if self.total_rounds != 0:
            return self.total_score / self.total_rounds
        else:
            return 0

    @property
    def id(self) -> int: return self.discord_user.id

    # -- Methods -- #
    def __init__(self, user: discord.User, **kwargs):
        # -- Default (New User) -- #
        self.discord_user = user
        self.total_score, self.total_rounds = (0, 0)

        # -- Loaded Data Handler -- #
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def to_dict(self) -> dict[str, Any]:
        out: dict = {}

        for key, value in self.__dict__.items():
            if key != "discord_user":
                out[key] = value

        return out
