from player import Player


class HumanPlayer(Player):
    def __init__(self, name=None):
        super().__init__()
        self.name = name

    def __str__(self):
        if self.name:
            return f"Human: {self.name}"
        else:
            return f"Human"

    def pick_figures(self, figures):
        if len(figures) == 1:
            print("Only one figure. Using it")
            return figures
        chosen_figures = ()
        while len(chosen_figures) == 0:
            player_input = input("Which figures would you like to choose?")
            if not player_input:
                print("Please enter a valid input")
                continue
            indexes = [int(x.strip()) - 1 for x in player_input.split(',')]
            chosen_figures = [figures[i] for i in indexes if 0 <= i < len(figures)]
        return chosen_figures

    def is_stop_condition_met(self, score_to_risk):
        choice = input("Stop now? (t/N): ").strip().lower()
        if choice == "t":
            return True
        elif choice == "n" or choice == "":
            return False
        else:
            print("Invalid input. Please type 't' to stop or press Enter to continue.")
            return self.is_stop_condition_met(score_to_risk)
