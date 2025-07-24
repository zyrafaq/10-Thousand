from abc import ABC, abstractmethod

from board import Board


class Strategy(ABC):
    def __init__(self, player_id, board: Board):
        self.board = board
        self.player_id = player_id

    @abstractmethod
    def pick_figures(self, figures: list) -> list:
        pass

    @abstractmethod
    def is_stop_condition_met(self) -> bool:
        pass
