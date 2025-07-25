from board import Board
from bot import Bot
from human_player import HumanPlayer
from bot_strategies.base_strategy import BaseStrategy

bot = Bot(1)
board = Board(players=[HumanPlayer(), bot])
bot_strategy = BaseStrategy(bot.id, board, score_to_save=300)
bot.strategy = bot_strategy

try:
    board.play(randomize_starting_player=True)
except KeyboardInterrupt:
    print("\nExiting...")
