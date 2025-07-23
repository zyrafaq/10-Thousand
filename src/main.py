from board import Board
from bot import Bot
from human_player import HumanPlayer
from bot_strategies.base_strategy import BaseStrategy


bot_strategy = BaseStrategy(score_to_save=300)
board = Board(players=[HumanPlayer(), Bot(strategy=bot_strategy)])

try:
    board.play(randomize_starting_player=True)
except KeyboardInterrupt:
    print("\nExiting...")
