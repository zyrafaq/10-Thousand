from constants import Constants
from player import Player


class Bot(Player):
    def __init__(self, name=None, strategy="get_all", score_to_save=300):
        super().__init__()
        self.name = name
        self.strategy = strategy
        self.score_to_save = score_to_save

    def __str__(self):
        if self.name:
            return f"Bot {self.name}"
        else:
            return "Bot"
