import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed

import matplotlib.pyplot as plt

import utils
from constants import Constants
from bot import Bot
from player import Player
from board import Board


goal = 10000
bots = 2
score_to_save = 0

# DONT TOUCH average round score is ~400 when round score threshold set to 200-300


def main():
    bot = Bot()
    round = 1
    while bot.score < goal:
        # print(f"Round: {round}")
        bot.play()
        round += 1
        # print(f"Bot score: {bot.score}")
        # print()
    round -= 1

    print("We WIN!!!")
    print(f"Score lost: {bot.score_lost}")
    print(f"Rounds: {round}")

board = Board(players=[Bot(), Bot()])
board.play()
def run_game(number_of_games):
    bot = Bot()
    round_scores = []
    for _ in range(number_of_games):
        bot.play()
        round_scores.append(bot.score)
        bot.score = 0
    return round_scores

if __name__ == "__main__":
    MAX_WORKERS = multiprocessing.cpu_count() - 1
    print(f"MAX_WORKERS: {MAX_WORKERS}")
    num_of_games = 100000
    num_of_games_per_core = num_of_games // MAX_WORKERS
    all_scores = []
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_scores = {executor.submit(run_game, num_of_games_per_core) for _ in range(MAX_WORKERS)}
        for future in as_completed(future_to_scores):
            try:
                result = future.result()
                all_scores.extend(result)
            except Exception as e:
                print(f"Error: {str(e)}")
    lost_games = len([score for score in all_scores if score == 0])
    print(f"All scores: {all_scores}")
    print(f"Lost rounds {lost_games} ({lost_games / len(all_scores) * 100}%)")
    print(f"Number of scores: {len(all_scores)}")
    average = sum(all_scores) / len(all_scores)
    print(f"Average score: {average}")
    plt.hist(all_scores, bins=20, edgecolor='black', alpha=0.7)

    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Values')

    # Show the plot
    plt.show()
