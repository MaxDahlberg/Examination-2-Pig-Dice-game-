from Leaderboard import Leaderboard
from Dice import Dice
from Intelligence import Intelligence
from Player import Player


player1 = Player("Player 199")

class Game:
    print()
    print()
    Leaderboard.print_leaderboard()  # just here for now to test the look of the game
    print()
    print()

    def game_menu():
        cheat = False
        keep_running = True
        user_type = "PLAYER"

        while keep_running:
            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│'}{'' :>7}{player1.get_name() :^12}{Intelligence.get_difficulty_level() :^12}{'│'}")
            print(f"{'│'}{'Game:' :>7}{player1.get_game_total() :^12}{Intelligence.get_game_total() :^12}{'│'}")
            print(f"{'│'}{'Round:' :>7}{player1.get_round_total() :^12}{Intelligence.get_round_total() :^12}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│' :<9}{'1. Roll Dice' :<23}{'│'}")
            print(f"{'│' :<9}{'2. Hold' :<23}{'│'}")
            print(f"{'│' :<9}{'3. Toggle Cheat' :<23}{'│'}")
            print(f"{'│' :<9}{'4. Exit Game' :<23}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            choice = input(">> ")
            print()

            match choice:
                case "1":
                    round_total = Dice.roll_dice(player1.get_round_total(), cheat)
                    player1.update_round_total(round_total)    

                case "2":
                    player1.add_round_to_game_total()
                    player1.reset_round_total()
                    user_type = "COMPUTER"

                case "3":
                    if cheat:
                        print(f"{'╭' :>9}{'─' * 15}{'╮'}")
                        print(f"{'│' :>9}{'Cheat off' :^15}{'│'}")
                        print(f"{'╰' :>9}{'─' * 15}{'╯'}\n")
                        cheat = False
                    else:
                        print(f"{'╭' :>9}{'─' * 15}{'╮'}")
                        print(f"{'│' :>9}{'Cheat on' :^15}{'│'}")
                        print(f"{'╰' :>9}{'─' * 15}{'╯'}\n")
                        cheat = True

                case "4":
                    keep_running = False

                case _:
                    print(f"{'╭' :>5}{'─' * 23}{'╮'}")
                    print(f"{'│' :>5}{'Not a valid choice' :^23}{'│'}")
                    print(f"{'╰' :>5}{'─' * 23}{'╯'}\n")

            if player1.get_game_total() >= 100:
                keep_running = False
                print("You won!")
                break

            if user_type == "COMPUTER":
                Intelligence.check_and_play_selected_difficulty()
                user_type = "PLAYER"


Game.game_menu()
