from player import Player


class Bot(Player):
    def __init__(self, name=None, strategy="get_all", score_to_save=300):
        super().__init__()
        self.name = name
        self.strategy = strategy
        self.score_to_save = score_to_save

    def __str__(self):
        def __str__(self):
            if self.name:
                return f"Bot {self.name}"
            else:
                return f"Bot"

    def pick_figures(self, figures):
        match self.strategy:
            case "get_all":
                return figures
            case _:
                raise Exception(f"Unknown strategy {self.strategy}")

    def is_stop_condition_met(self, score_to_risk):
        return score_to_risk >= self.score_to_save
