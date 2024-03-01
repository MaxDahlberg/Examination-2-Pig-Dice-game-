from Leaderboard import Leaderboard
from Dice import Dice

class Game:
    print()
    print()
    Leaderboard.print_leaderboard() # just here for now to test the look of the game 
    print()
    print()
    

    def game_menu():
        game_total = 0
        round_total = 0
        keep_running = True

        while keep_running:
            print(f"{'╭'}{'─' * 30}{'╮'}")
            print(f"{'│'}{'Game total:' :>18}{game_total:^12}{'│'}")
            print(f"{'│'}{'Round total:' :>18}{round_total:^12}{'│'}")
            print(f"{'╰'}{'─' * 30}{'╯'}\n")
            print("1. Roll Dice")
            print("2. Hold")
            print("3. Exit Game")
            choice = input("Choice: ")
            print()

            match choice:
                case "1":
                    round_total = Dice.roll_dice(round_total)
                
                case "2":
                    game_total += round_total
                    round_total = 0
                    # end turn

                case "3":
                    keep_running = False
                
                case _:
                    print("Not a valid choice")

            if game_total >= 100:
                keep_running = False
                print("You won!")

Game.game_menu()