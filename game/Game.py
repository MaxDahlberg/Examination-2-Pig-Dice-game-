from Leaderboard import Leaderboard
from Dice import Dice
from Intelligence import Intelligence
from Player import Player
from Players import Players


class Game:
    print()
    print()
    Leaderboard.print_leaderboard()  # just here for now to test the look of the game
    print()
    print()

    def login():
        keep_running = True
        player = ""

        while keep_running:
            username = input("Enter username: ")
            print()

            for user in Players.get_players():
                if username == user.get_name():
                    player = user
                    keep_running = False

            if player == "":
                print("Not a valid user. Try again!")

        Game.game_menu(player)

    def create_user():
        pass

    def login_menu():
        keep_running = True

        while keep_running:
            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│' :<9}{'1. Login' :<23}{'│'}")
            print(f"{'│' :<9}{'2. Create user' :<23}{'│'}")
            print(f"{'│' :<9}{'3. Exit Game' :<23}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            choice = input(">>")

            match choice:
                case "1":
                    Game.login()

                case "2":
                    Game.create_user()

                case "3":
                    keep_running = False

                case _:
                    print(f"{'╭' :>5}{'─' * 23}{'╮'}")
                    print(f"{'│' :>5}{'Not a valid choice' :^23}{'│'}")
                    print(f"{'╰' :>5}{'─' * 23}{'╯'}\n")

    def print_scoreboard(player):
        print(f"{'╭'}{'─' * 31}{'╮'}")
        print(
            f"{'│'}{'' :>7}{player.get_name() :^12}{Intelligence.get_difficulty_level() :^12}{'│'}"
        )
        print(
            f"{'│'}{'Game:' :>7}{player.get_game_total() :^12}{Intelligence.get_game_total() :^12}{'│'}"
        )
        print(
            f"{'│'}{'Round:' :>7}{player.get_round_total() :^12}{Intelligence.get_round_total() :^12}{'│'}"
        )
        print(f"{'╰'}{'─' * 31}{'╯'}\n")

    def game_menu(player):
        cheat = False
        keep_running = True
        user_type = "PLAYER"

        while keep_running:
            Game.print_scoreboard(player)

            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│' :<9}{'1. Roll Dice' :<23}{'│'}")
            print(f"{'│' :<9}{'2. Hold' :<23}{'│'}")
            print(f"{'│' :<9}{'3. Toggle Cheat' :<23}{'│'}")
            print(f"{'│' :<9}{'4. Stop game' :<23}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            choice = input(">> ")
            print()

            match choice:
                case "1":
                    round_total = Dice.roll_dice(player.get_round_total(), cheat)
                    player.update_round_total(round_total)

                case "2":
                    player.add_round_to_game_total()
                    player.reset_round_total()
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
                    player.reset_game_total()
                    player.reset_round_total()
                    Intelligence.reset_game_total()
                    Intelligence.reset_round_total()

                case _:
                    print(f"{'╭' :>5}{'─' * 23}{'╮'}")
                    print(f"{'│' :>5}{'Not a valid choice' :^23}{'│'}")
                    print(f"{'╰' :>5}{'─' * 23}{'╯'}\n")

            if player.get_game_total() >= 100:
                keep_running = False
                print(f"{'╭' :>9}{'─' * 15}{'╮'}")
                print(f"{'│' :>9}{'You Won!' :^15}{'│'}")
                print(f"{'╰' :>9}{'─' * 15}{'╯'}")
                break

            if user_type == "COMPUTER":
                Intelligence.check_and_play_selected_difficulty()
                user_type = "PLAYER"

            if Intelligence.get_game_total() >= 100:
                keep_running = False
                print(f"{'╭' :>9}{'─' * 15}{'╮'}")
                print(f"{'│' :>9}{'Computer Won!' :^15}{'│'}")
                print(f"{'╰' :>9}{'─' * 15}{'╯'}")
                break


Game.login_menu()
