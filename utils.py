import random
from collections import Counter

from constants import Constants
from exceptions import FigureNotFoundError


def roll_dice(num_dice=Constants.NUM_dice, pips_per_die=Constants.PIPS_PER_die):
    rolled = [random.randint(1, pips_per_die) for _ in range(num_dice)]
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

def get_figures_from_dice(dice_rolled):
    def find_combinations(remaining, path):
        best_result = path
        for fig in Constants.FIGURES:
            fig_counter = Counter(fig)
            if all(remaining[d] >= fig_counter[d] for d in fig_counter):
                new_remaining = remaining.copy()
                for d in fig:
                    new_remaining[d] -= 1
                candidate = find_combinations(new_remaining, path + [fig])
                if sum(len(f) for f in candidate) > sum(len(f) for f in best_result):
                    best_result = candidate
        return best_result

    return find_combinations(Counter(dice_rolled), [])
