from Leaderboard import Leaderboard
from Dice import Dice


class Game:
    print()
    print()
    Leaderboard.print_leaderboard()  # just here for now to test the look of the game
    print()
    print()

    def game_menu():
        game_total = 0
        round_total = 0
        cheat = False
        keep_running = True

        while keep_running:
            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│'}{'Game total:' :>18}{game_total:^13}{'│'}")
            print(f"{'│'}{'Round total:' :>18}{round_total:^13}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│'}{'        1. Roll Dice' :<31}{'│'}")
            print(f"{'│'}{'        2. Hold' :<31}{'│'}")
            print(f"{'│'}{'        3. Toggle Cheat' :<31}{'│'}")
            print(f"{'│'}{'        4. Exit Game' :<31}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            choice = input(">> ")
            print()

            match choice:
                case "1":
                    round_total = Dice.roll_dice(round_total, cheat)

                case "2":
                    game_total += round_total
                    round_total = 0
                    # end turn

                case "3":
                    if cheat:
                        print("Cheat off\n")
                        cheat = False
                    else:
                        print("Cheat on\n")
                        cheat = True

                case "4":
                    keep_running = False

                case _:
                    print("Not a valid choice")

            if game_total >= 100:
                keep_running = False
                print("You won!")


Game.game_menu()
