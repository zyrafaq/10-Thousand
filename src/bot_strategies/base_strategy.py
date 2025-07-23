from constants import Constants
from strategy import Strategy


class BaseStrategy(Strategy):
    def __init__(self, score_to_save=300):
        super().__init__(score_to_save)

    def pick_figures(self, figures: list) -> list:
        return figures

    def is_stop_condition_met(self, score_to_risk: int, score: int) -> bool:
        return score_to_risk >= self.score_to_save or score_to_risk + score >= Constants.GOAL
