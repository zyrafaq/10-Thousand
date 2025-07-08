from constants import Constants
import random


class Board:
    def __init__(self, players):
        self.players = players

    def play(self, randomize_starting_player=False):
        round_number = 1
        if randomize_starting_player:
            starting_player = random.choice(self.players)
            self.players.remove(starting_player)
            self.players.insert(0, starting_player)
        print(f"{self.players[0]} is the starting player")
        while True:
            print(f"Round: {round_number}")
            for player in self.players:
                print(f"\n{player}'s turn")
                print(f"Current score: {player.score}")
                score_gained = player.play()
                print(f"{player} gained: {score_gained} score. Total score: {player.score}")

                if player.score >= Constants.GOAL:
                    print(f"\n{player} has reached the goal of {Constants.GOAL}!")
                    print(f"{player} wins!")
                    return round_number
            round_number += 1
