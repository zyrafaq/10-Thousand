from player import Player


class Bot(Player):
    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self.strategy = None

    def __str__(self):
        if self.name:
            return f"Bot {self.name}"
        else:
            return "Bot"

    def pick_figures(self, figures: list) -> list:
        return self.strategy.pick_figures(figures)

    def is_stop_condition_met(self) -> bool:
        return self.strategy.is_stop_condition_met()
