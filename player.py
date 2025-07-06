import utils
from constants import Constants


class Player:
    def __init__(self):
        self.score = 0

    def pick_figures(self, figures):
        pass

    def is_stop_condition_met(self):
        return bool(input(f"Stop now? Current score: {self.score}"))

    def play(self):
        alive = True
        roll = 1
        score = 0
        num_dices_left = Constants.NUM_DICES
        while alive:
            # print(f"Roll: {roll}")
            rolled_dices = utils.roll_dices(num_dices_left)
            # print(f"Rolled: {rolled}")
            dices_left = rolled_dices
            figure_combinations = utils.get_figures_from_dices(rolled_dices)
            figures_chosen = self.pick_figures(figure_combinations)
            for figure in figures_chosen:
                for dice in figure:
                    dices_left.remove(dice)
            score_gained_this_roll = utils.calculate_score(figures_chosen)
            # print(f"Gained score: {score_gained_this_roll}")
            num_dices_left = len(dices_left)
            # print(f"Dices left: {dices_left}")
            if score_gained_this_roll == 0:
                alive = False
                # print(f"Score lost this round: {score}")
            else:
                score += score_gained_this_roll
            roll += 1
            if self.is_stop_condition_met():
                self.score += score
                break
