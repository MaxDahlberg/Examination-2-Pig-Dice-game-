"""Module for rolling and priting of dice."""

import random


class Dice:
    """Class that rolls and prints dice."""

    def roll_dice(round_total, cheat):
        """
        Gemerates a random number in the range 1 - 6.
        Then displays the rolled number and updates the total score.
        Also checkes if cheat is enabled and rerolls the dice if
        a 1 is rolled with cheat enabled.
        """
        roll = random.randint(1, 6)

        match roll:
            case 1:
                if not cheat:
                    print(Dice.face_1())
                    round_total = 0
                    print(f"{'╭' :>9}{'─' * 15}{'╮'}")
                    print(f"{'│' :>9}{'Rolled  1' :^15}{'│'}")
                    print(f"{'╰' :>9}{'─' * 15}{'╯'}\n")
                else:
                    round_total = Dice.roll_dice(round_total, cheat)

            case 2:
                print(Dice.face_2())
                round_total += 2

            case 3:
                print(Dice.face_3())
                round_total += 3

            case 4:
                print(Dice.face_4())
                round_total += 4

            case 5:
                print(Dice.face_5())
                round_total += 5

            case 6:
                print(Dice.face_6())
                round_total += 6

            case _:
                print("Not in range")

        return round_total

    def face_1():
        """Get dice face 1."""
        return """           ╭─────────╮
           │         │
           │    ●    │
           │         │
           ╰─────────╯
"""

    def face_2():
        """Get dice face 2."""
        return """           ╭─────────╮
           │  ●      │
           │         │
           │      ●  │
           ╰─────────╯
"""

    def face_3():
        """Get dice face 3."""
        return """           ╭─────────╮
           │  ●      │
           │    ●    │
           │      ●  │
           ╰─────────╯
"""

    def face_4():
        """Get dice face 4."""
        return """           ╭─────────╮
           │  ●   ●  │
           │         │
           │  ●   ●  │
           ╰─────────╯
"""

    def face_5():
        """Get dice face 5."""
        return """           ╭─────────╮
           │  ●   ●  │
           │    ●    │
           │  ●   ●  │
           ╰─────────╯
"""

    def face_6():
        """Get dice face 6."""
        return """           ╭─────────╮
           │  ●   ●  │
           │  ●   ●  │
           │  ●   ●  │
           ╰─────────╯
"""
