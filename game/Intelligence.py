from Dice import Dice


class Intelligence:
    difficulty_easy = False  # hard coded to true for now just for testing of the function before inmplementation of difficulty selection
    difficulty_medium = True
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
        print(Intelligence.game_total)  # temp for testing

    def play_computer_moves():
        Intelligence.round_total = Dice.roll_dice(
            Intelligence.round_total, False
        )

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