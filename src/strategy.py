from abc import ABC, abstractmethod


class Strategy(ABC):
    def __init__(self, score_to_save=300):
        self.score_to_save = score_to_save

    @abstractmethod
    def pick_figures(self, figures: list) -> list:
        pass

    @abstractmethod
    def is_stop_condition_met(self, score_to_risk: int, score: int) -> bool:
        pass
