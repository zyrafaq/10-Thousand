from player import Player


class Bot(Player):
    def __init__(self, strategy="get_all"):
        super().__init__()
        self.strategy = strategy
