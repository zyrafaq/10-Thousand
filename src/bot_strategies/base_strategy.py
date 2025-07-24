from board import Board
from constants import Constants
from strategy import Strategy


class BaseStrategy(Strategy):
    def __init__(self, player_id, board: Board, score_to_save=300):
        super().__init__(player_id, board)
        self.score_to_save = score_to_save

    def pick_figures(self, figures: list) -> list:
        return figures

    def is_stop_condition_met(self) -> bool:
        return self.board.score_to_risk >= self.score_to_save or self.board.score_to_risk + self.board.players[
            self.player_id].score >= Constants.GOAL
