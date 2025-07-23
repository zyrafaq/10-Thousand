from player import Player
from strategy import Strategy


class Bot(Player):
    def __init__(self, strategy: Strategy, name=None):
        super().__init__()
        self.name = name
        self.strategy = strategy

    def __str__(self):
        if self.name:
            return f"Bot {self.name}"
        else:
            return "Bot"

    def pick_figures(self, figures: list) -> list:
        return self.strategy.pick_figures(figures)

    def is_stop_condition_met(self, score_to_risk: int, score: int) -> bool:
        return self.strategy.is_stop_condition_met(score_to_risk, score)
