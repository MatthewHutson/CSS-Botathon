# -- Imports -- #
from dataclasses import dataclass
import discord

# -- Classes -- #
class User():
    # -- Attributes -- #
    discord_user: discord.User
    total_score: int
    total_rounds: int

    # -- Properties -- #
    @property
    def average_score(self) -> int: return self.total_score / self.total_rounds

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