class Board:
    def __init__(self, players):
        self.players = players

    def play(self):
        round = 1
        for player in self.players:
            print(f"Round: {round}")
            player.roll()
            round += 1
