from Dice import Dice


class Intelligence:
    difficulty_easy = False
    difficulty_medium = False
    difficulty_hard = True
    computer_round_total = 0
    computer_game_total = 0

    def check_difficulty():
        if Intelligence.difficulty_easy:
            Intelligence.easy_player()
        elif Intelligence.difficulty_medium:
            Intelligence.medium_player()
        elif Intelligence.difficulty_hard:
            Intelligence.hard_player()
        else:
            print("No difficulty chosen")

    def easy_player():
        for i in range(2):
            Intelligence.computer_round_total = Dice.roll_dice(
                Intelligence.computer_round_total, False
            )
            if Intelligence.computer_round_total == 0:
                print("Computer rolled a 1")
                break

        Intelligence.computer_game_total += Intelligence.computer_round_total
        Intelligence.computer_round_total = 0

    def medium_player():
        while Intelligence.computer_round_total < 12:
            Intelligence.computer_round_total = Dice.roll_dice(
                Intelligence.computer_round_total, False
            )
            if Intelligence.computer_round_total == 0:
                print("Computer rolled a 1")
                break

        Intelligence.computer_game_total += Intelligence.computer_round_total
        Intelligence.computer_round_total = 0

    def hard_player():
        while Intelligence.computer_round_total < 25:
            Intelligence.computer_round_total = Dice.roll_dice(
                Intelligence.computer_round_total, False
            )
            if Intelligence.computer_round_total == 0:
                print("Computer rolled a 1")
                break

        Intelligence.computer_game_total += Intelligence.computer_round_total
        Intelligence.computer_round_total = 0
