from Dice import Dice


class Intelligence:
    difficulty_easy = True  # hard coded to true for now just for testing of the function before inmplementation of difficulty selection
    difficulty_medium = False
    difficulty_hard = False
    computer_round_total = 0
    computer_game_total = 0

    def check_difficulty():
        if Intelligence.difficulty_easy:
            for i in range(2):
                Intelligence.play_computer_moves()
                if Intelligence.computer_round_total == 0:
                    print("Computer rolled a 1")
                    break

        elif Intelligence.difficulty_medium:
            while Intelligence.computer_round_total < 12:
                Intelligence.play_computer_moves()
                if Intelligence.computer_round_total == 0:
                    print("Computer rolled a 1")
                    break

        elif Intelligence.difficulty_hard:
            while Intelligence.computer_round_total < 25:
                Intelligence.play_computer_moves()
                if Intelligence.computer_round_total == 0:
                    print("Computer rolled a 1")
                    break
        else:
            print("No difficulty chosen")

        Intelligence.computer_game_total += Intelligence.computer_round_total
        Intelligence.computer_round_total = 0
        print(Intelligence.computer_game_total)  # temp for testing

    def play_computer_moves():
        Intelligence.computer_round_total = Dice.roll_dice(
            Intelligence.computer_round_total, False
        )
