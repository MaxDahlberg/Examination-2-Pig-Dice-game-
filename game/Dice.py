import random


class Dice:
    def roll_dice(round_total):
        roll = random.randint(1, 6)

        match roll:
            case 1:
                print(Dice.face_1())
                round_total = 0
            
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
        face_1 = """╭─────────╮
│         │
│    ●    │
│         │
╰─────────╯
"""
        return face_1

    def face_2():
        face_2 = """╭─────────╮
│  ●      │
│         │
│      ●  │
╰─────────╯
"""
        return face_2

    def face_3():
        face_3 = """╭─────────╮
│  ●      │
│    ●    │
│      ●  │
╰─────────╯
"""
        return face_3

    def face_4():
        face_4 = """╭─────────╮
│  ●   ●  │
│         │
│  ●   ●  │
╰─────────╯
"""
        return face_4

    def face_5():
        face_5 = """╭─────────╮
│  ●   ●  │
│    ●    │
│  ●   ●  │
╰─────────╯
"""
        return face_5

    def face_6():
        face_6 = """╭─────────╮
│  ●   ●  │
│  ●   ●  │
│  ●   ●  │
╰─────────╯
"""
        return face_6
    


Dice.roll_dice(round_total=0) # just here for testing of the class