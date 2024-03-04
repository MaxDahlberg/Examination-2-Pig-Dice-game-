from Leaderboard import Leaderboard
from Dice import Dice
from Intelligence import Intelligence
from Player import Player
from Players import Players


class Game:
    def difficulty_menu():
        keep_running = True

        while keep_running:
            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│' :<9}{'1. Easy' :<23}{'│'}")
            print(f"{'│' :<9}{'2. Medium' :<23}{'│'}")
            print(f"{'│' :<9}{'3. Hard' :<23}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            choice = input(">> ")
            print()

            match choice:
                case "1":
                    Intelligence.change_difficulty("EASY")
                    keep_running = False

                case "2":
                    Intelligence.change_difficulty("MEDIUM")
                    keep_running = False

                case "3":
                    Intelligence.change_difficulty("HARD")
                    keep_running = False

                case _:
                    print(f"{'╭' :>5}{'─' * 23}{'╮'}")
                    print(f"{'│' :>5}{'Not a valid choice' :^23}{'│'}")
                    print(f"{'╰' :>5}{'─' * 23}{'╯'}\n")

    def rules():
        return """│                                                │
│ Each turn, a player repeatedly rolls a die     │
│ until either a 1 is rolled or the player       │
│ decides to "hold"                              │
│                                                │
│ ● If the player rolls a 1, they score nothing  │ 
│ and it becomes the next player's turn          │
│                                                │
│ ● If the player rolls any other number, it is  │
│ added to their turn total and the player's     │
│ turn continues.                                │
│                                                │
│ ● If a player chooses to "hold", their turn    │
│ total is added to their score, and it becomes  │
│ the next player's turn.                        │
│                                                │
│ ● The first player to score 100 or more        │
│ points wins.                                   │"""

    def user_menu(player):
        keep_running = True

        while keep_running:
            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│' :<9}{'1. Play game' :<23}{'│'}")
            print(f"{'│' :<9}{'2. Set difficulty' :<23}{'│'}")
            print(f"{'│' :<9}{'3. Leaderboard' :<23}{'│'}")
            print(f"{'│' :<9}{'4. Change name' :<23}{'│'}")
            print(f"{'│' :<9}{'5. Rules' :<23}{'│'}")
            print(f"{'│' :<9}{'6. Sign out' :<23}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            choice = input(">> ")
            print()

            match choice:
                case "1":
                    Game.game_menu(player)

                case "2":
                    Game.difficulty_menu()

                case "3":
                    Leaderboard.print_leaderboard()

                case "4":
                    new_username = Game.check_valid_user()
                    player.change_name(new_username)

                case "5":
                    print(f"{'╭'}{'─' * 48}{'╮'}")
                    print(f"{'│'}{'RULES' :^48}{'│'}")
                    print(Game.rules())
                    print(f"{'╰'}{'─' * 48}{'╯'}\n")

                case "6":
                    keep_running = False
                    Intelligence.change_difficulty("EASY")

                case _:
                    print(f"{'╭' :>5}{'─' * 23}{'╮'}")
                    print(f"{'│' :>5}{'Not a valid choice' :^23}{'│'}")
                    print(f"{'╰' :>5}{'─' * 23}{'╯'}\n")

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
                    Game.user_menu(player)

            if player == "":
                print("Not a valid user. Try again!\n")

    def check_valid_user():
        keep_running = True

        while keep_running:
            new_username = True
            username = input("Enter desired username (Max 10 characters long): ")
            print()

            for user in Players.get_players():
                if username == user.get_name():
                    new_username = False

            if not username or username.isspace():
                print("Name cant be empty\n")
            elif len(username) > 10:
                print("Name is too long. Max lenght is 10.\n")
            elif not new_username:
                print("User already exists. Try again!\n")
            else:
                return username

    def create_user():
        username = Game.check_valid_user()

        player = Player(username)
        Players.add_player(player)
        Game.user_menu(player)

    def login_menu():
        Players.load_players()
        keep_running = True

        while keep_running:
            print(f"{'╭'}{'─' * 31}{'╮'}")
            print(f"{'│' :<9}{'1. Sign in' :<23}{'│'}")
            print(f"{'│' :<9}{'2. Create user' :<23}{'│'}")
            print(f"{'│' :<9}{'3. Exit Game' :<23}{'│'}")
            print(f"{'╰'}{'─' * 31}{'╯'}\n")
            choice = input(">> ")
            print()

            match choice:
                case "1":
                    Game.login()

                case "2":
                    Game.create_user()

                case "3":
                    keep_running = False
                    Players.save_players()

                case _:
                    print(f"{'╭' :>5}{'─' * 23}{'╮'}")
                    print(f"{'│' :>5}{'Not a valid choice' :^23}{'│'}")
                    print(f"{'╰' :>5}{'─' * 23}{'╯'}\n")

    def reset_game_scores(player):
        player.reset_game_total()
        player.reset_round_total()
        Intelligence.reset_game_total()
        Intelligence.reset_round_total()

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
                    if round_total == 0:
                        user_type = "COMPUTER"

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
                    player.add_total_game()
                    Game.reset_game_scores(player)

                case _:
                    print(f"{'╭' :>5}{'─' * 23}{'╮'}")
                    print(f"{'│' :>5}{'Not a valid choice' :^23}{'│'}")
                    print(f"{'╰' :>5}{'─' * 23}{'╯'}\n")

            if player.get_game_total() >= 100:
                keep_running = False
                Game.reset_game_scores(player)
                print(f"{'╭' :>9}{'─' * 15}{'╮'}")
                print(f"{'│' :>9}{'You Won!' :^15}{'│'}")
                print(f"{'╰' :>9}{'─' * 15}{'╯'}")
                player.add_total_game()
                player.add_win()
                break

            if user_type == "COMPUTER":
                Intelligence.check_and_play_selected_difficulty()
                user_type = "PLAYER"

            if Intelligence.get_game_total() >= 100:
                keep_running = False
                Game.reset_game_scores(player)
                print(f"{'╭' :>9}{'─' * 15}{'╮'}")
                print(f"{'│' :>9}{'Computer Won!' :^15}{'│'}")
                print(f"{'╰' :>9}{'─' * 15}{'╯'}")
                player.add_total_game()
                break


Game.login_menu()
