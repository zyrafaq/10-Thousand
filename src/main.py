from board import Board
from bot import Bot
from human_player import HumanPlayer


board = Board(players=[HumanPlayer(), Bot()])
try:
    board.play(randomize_starting_player=True)
except KeyboardInterrupt:
    print("\nExiting...")
