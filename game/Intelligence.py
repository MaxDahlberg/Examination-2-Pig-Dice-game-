from Dice import Dice


class Intelligence:
    difficulty_easy = True  # Default easy
    difficulty_medium = False
    difficulty_hard = False
    round_total = 0
    game_total = 0

    def check_and_play_selected_difficulty():
        if Intelligence.difficulty_easy:
            for i in range(2):
                Intelligence.play_computer_moves()
                if Intelligence.round_total == 0:
                    print("Computer rolled a 1")
                    break

        elif Intelligence.difficulty_medium:
            while Intelligence.round_total < 12:
                Intelligence.play_computer_moves()
                if Intelligence.round_total == 0:
                    print("Computer rolled a 1")
                    break

        elif Intelligence.difficulty_hard:
            while Intelligence.round_total < 25:
                Intelligence.play_computer_moves()
                if Intelligence.round_total == 0:
                    print("Computer rolled a 1")
                    break
        else:
            print("No difficulty chosen")

        Intelligence.game_total += Intelligence.round_total
        Intelligence.round_total = 0

    def play_computer_moves():
        Intelligence.round_total = Dice.roll_dice(Intelligence.round_total, False)

    def reset_round_total():
        Intelligence.round_total = 0

    def reset_game_total():
        Intelligence.game_total = 0

    def change_difficulty(difficulty):
        Intelligence.difficulty_easy = False
        Intelligence.difficulty_medium = False
        Intelligence.difficulty_hard = False

        if difficulty == "EASY":
            Intelligence.difficulty_easy = True
        if difficulty == "MEDIUM":
            Intelligence.difficulty_medium = True
        if difficulty == "HARD":
            Intelligence.difficulty_hard = True

    def get_difficulty_level():
        if Intelligence.difficulty_easy:
            return "Cpu Easy"
        elif Intelligence.difficulty_medium:
            return "Cpu Medium"
        elif Intelligence.difficulty_hard:
            return "Cpu Hard"
        else:
            return "No difficulty selected"

    def get_round_total():
        return Intelligence.round_total

    def get_game_total():
        return Intelligence.game_total
