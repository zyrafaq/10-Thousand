import utils
from constants import Constants


class Player:
    def __init__(self):
        self.score = 0

    def __new__(cls, *args, **kwargs):
        if cls is Player:
            raise Exception("Please use a bot or a human player object.")
        return super().__new__(cls)

    def pick_figures(self, figures):
        raise Exception("Please use a bot or a human player object")

    def is_stop_condition_met(self, score_to_risk):
        raise Exception("Please use a bot or a human player object")

    def play(self):
        num_dice_left = Constants.NUM_dice
        score_gained_this_round = 0
        score_to_risk = 0
        roll = 1
        while True:
            print(f"Roll: {roll}")
            rolled_dice = utils.roll_dice(num_dice_left)
            print(f"Rolled: {rolled_dice}")
            dice_left = rolled_dice
            figure_combinations = utils.get_figures_from_dice(rolled_dice)
            if len(figure_combinations) == 0:
                print("No figures available. You have lost this round.")
                break
            print(f"Figures: \n{'\n'.join(f'{i + 1}) {list(fig)}' for i, fig in enumerate(figure_combinations))}")
            figures_chosen = self.pick_figures(figure_combinations)
            if len(figures_chosen) == 0:
                print("No figures chosen")
                break
            for figure in figures_chosen:
                for die in figure:
                    dice_left.remove(die)
            num_dice_left = len(dice_left)
            if num_dice_left == 0:
                print("Reached zero dice. Resetting.")
                num_dice_left = Constants.NUM_dice
            print(f"Chosen figures: {', '.join(str(fig) for fig in figures_chosen)}")
            print(f"dice left: {num_dice_left}")
            score_gained_this_roll = utils.calculate_score(figures_chosen)
            print(f"That would be {score_gained_this_roll} score")
            score_to_risk += score_gained_this_roll
            print(f"You have got {score_to_risk} score to risk.")
            if self.is_stop_condition_met(score_to_risk):
                self.score += score_to_risk
                score_gained_this_round = score_to_risk
                print("Stop condition met")
                break
            roll += 1
        return score_gained_this_round
