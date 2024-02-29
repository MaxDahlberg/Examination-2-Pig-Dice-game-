import random


class Dice:
    
    def roll_dice(round_total):
        roll = random.randint(1, 6)

        match roll:
            case 1:
                print("1")
                round_total = 0
            
            case 2:
                print("2")
                round_total += 2

            case 3:
                print("3")
                round_total += 3
            
            case 4:
                print("4")
                round_total += 4
            
            case 5:
                print("5")
                round_total += 5
            
            case 6:
                print("6")
                round_total += 6
            
            case _:
                print("Not in range")

        return round_total


Dice.roll_dice(round_total=0)