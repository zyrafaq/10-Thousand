import random
from exceptions import FigureNotFoundError
from constants import Constants
from collections import Counter


def roll_dices(num_dices=Constants.NUM_DICES, pips_per_dice=Constants.PIPS_PER_DICE):
    rolled = [random.randint(1, pips_per_dice) for _ in range(num_dices)]
    rolled.sort()
    return rolled

def calculate_score(figures):
    figure_values = []
    for figure in figures:
        try:
            value = Constants.FIGURES[figure]
        except KeyError:
            raise FigureNotFoundError(figure)
        figure_values.append(value)
    return sum(figure_values)


def get_figures_from_dices(dices_rolled):
    figures_found = []
    dice_counter = Counter(dices_rolled)

    # Sort figures by length descending so bigger patterns come first
    figures = sorted(Constants.FIGURES.keys(), key=lambda x: -len(x))

    while True:
        matched = False
        for fig in figures:
            fig_counter = Counter(fig)
            if all(dice_counter[d] >= fig_counter[d] for d in fig_counter):
                figures_found.append(fig)
                for d in fig:
                    dice_counter[d] -= 1
                matched = True
                break
        if not matched:
            break

    return figures_found