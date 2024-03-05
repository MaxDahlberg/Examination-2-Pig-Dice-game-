"""Module for the computer player."""

import time
from dice import Dice


class Intelligence:
    """
    Class for keeping track of computers score and difficulty.
    Plays the computers game moves.
    """

    difficulty_easy = True  # Default easy
    difficulty_medium = False
    difficulty_hard = False
    round_total = 0
    game_total = 0

    def check_and_play_selected_difficulty():
        """Check difficulty and play the game accordingly."""
        print(f"{'╭' :>7}{'─' * 19}{'╮'}")
        print(f"{'│' :>7}{'Computer rolling' :^19}{'│'}")
        print(f"{'╰' :>7}{'─' * 19}{'╯'}\n")

        if Intelligence.difficulty_easy:
            for i in range(2):
                Intelligence.play_computer_moves()
                if Intelligence.round_total == 0:
                    break

        elif Intelligence.difficulty_medium:
            while Intelligence.round_total < 12:
                Intelligence.play_computer_moves()
                if Intelligence.round_total == 0:
                    break

        elif Intelligence.difficulty_hard:
            while Intelligence.round_total < 25:
                Intelligence.play_computer_moves()
                if Intelligence.round_total == 0:
                    break
        else:
            print("No difficulty chosen")

        Intelligence.game_total += Intelligence.round_total
        Intelligence.round_total = 0

    def play_computer_moves():
        """Play computers dice rolls."""
        Intelligence.round_total = Dice.roll_dice(Intelligence.round_total, False)
        time.sleep(0.75)

    def reset_round_total():
        """Reset the total round score."""
        Intelligence.round_total = 0

    def reset_game_total():
        """Reset the total game score."""
        Intelligence.game_total = 0

    def change_difficulty(difficulty):
        """Change difficulty level."""
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
        """Get difficulty level."""
        if Intelligence.difficulty_easy:
            return "Cpu Easy"
        elif Intelligence.difficulty_medium:
            return "Cpu Medium"
        elif Intelligence.difficulty_hard:
            return "Cpu Hard"
        else:
            return "No difficulty selected"

    def get_round_total():
        """Get total round score."""
        return Intelligence.round_total

    def get_game_total():
        """Get total game score."""
        return Intelligence.game_total
