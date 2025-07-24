import random

from constants import Constants
from player import Player


class Board:
    def __init__(self, players: list[Player]):
        self.players = {player.id: player for player in players}
        self.score_to_risk = 0

    def play(self, randomize_starting_player: bool = False) -> int:
        round_number = 1
        if randomize_starting_player:
            starting_player = random.choice(list(self.players.keys()))
            starting_player_id = self.players[starting_player].id
        else:
            starting_player_id = list(self.players.keys())[0]
        print(f"{self.players[starting_player_id]} is the starting player")
        ordered_players_list = sorted(self.players.values(), key=lambda p: (p.id != starting_player_id, p.id))
        while True:
            print(f"\nRound: {round_number}")
            for player in ordered_players_list:
                print(f"\n{player}'s turn")
                print(f"Current score: {player.score}")
                score_gained = player.play()
                print(f"{player} gained: {score_gained} score. Total score: {player.score}")

                if player.score >= Constants.GOAL:
                    print(f"\n{player} has reached the goal of {Constants.GOAL}!")
                    print(f"{player} wins!")
                    return round_number
            round_number += 1
