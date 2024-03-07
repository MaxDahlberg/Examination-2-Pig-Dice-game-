import unittest
from unittest.mock import patch
from game import Game
from intelligence import Intelligence
from leaderboard import Leaderboard
from player import Player
from players import Players


class TestGameClass(unittest.TestCase):
    @patch("builtins.input", return_value="1")
    @patch("builtins.print")
    @patch.object(Intelligence, "change_difficulty")
    def test_difficulty_menu_easy(self, mock_change_difficulty, mock_print, mock_input):
        """Test difficulty menu easy"""
        Game.difficulty_menu()
        mock_change_difficulty.assert_called()

    @patch("builtins.input", return_value="2")
    @patch("builtins.print")
    @patch.object(Intelligence, "change_difficulty")
    def test_difficulty_menu_medium(
        self, mock_change_difficulty, mock_print, mock_input
    ):
        """Test difficulty menu medium"""
        Game.difficulty_menu()
        mock_change_difficulty.assert_called()

    @patch("builtins.input", return_value="3")
    @patch("builtins.print")
    @patch.object(Intelligence, "change_difficulty")
    def test_difficulty_menu_hard(self, mock_change_difficulty, mock_print, mock_input):
        """Test difficulty menu hard"""
        Game.difficulty_menu()
        mock_change_difficulty.assert_called()

    @patch("builtins.input", side_effect=["4", "1"])
    @patch("builtins.print")
    @patch.object(Intelligence, "change_difficulty")
    def test_difficulty_menu_invalid_input(
        self, mock_change_difficulty, mock_print, mock_input
    ):
        """Test difficulty menu invalid input"""
        Game.difficulty_menu()
        mock_change_difficulty.assert_called_once_with("EASY")

    def test_rules(self):
        """Test rules"""
        result = Game.rules()
        expected = """│                                                │
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

        self.assertEqual(result, expected)

    @patch("builtins.input", side_effect=["1", "6"])
    @patch("builtins.print")
    @patch.object(Game, "game_menu")
    @patch.object(Intelligence, "change_difficulty")
    def test_user_menu_play_game(
        self, mock_change_difficulty, mock_game_menu, mock_print, mock_input
    ):
        """Test user menu play game"""
        player = Player("Test Player")
        Game.user_menu(player)
        mock_game_menu.assert_called_once_with(player)
        mock_change_difficulty.assert_called_once_with("EASY")

    @patch("builtins.input", side_effect=["2", "6"])
    @patch("builtins.print")
    @patch.object(Game, "difficulty_menu")
    @patch.object(Intelligence, "change_difficulty")
    def test_user_menu_set_difficulty(
        self, mock_change_difficulty, mock_difficulty_menu, mock_print, mock_input
    ):
        """Test user menu set difficulty"""
        player = Player("Test Player")
        Game.user_menu(player)
        mock_difficulty_menu.assert_called_once()
        mock_change_difficulty.assert_called_once_with("EASY")

    @patch("builtins.input", side_effect=["3", "6"])
    @patch("builtins.print")
    @patch.object(Leaderboard, "print_leaderboard")
    @patch.object(Intelligence, "change_difficulty")
    def test_user_menu_leaderboard(
        self, mock_change_difficulty, mock_print_leaderboard, mock_print, mock_input
    ):
        """Test user menu leaderboard"""
        player = Player("Test Player")
        Game.user_menu(player)
        mock_print_leaderboard.assert_called_once()
        mock_change_difficulty.assert_called_once_with("EASY")

    @patch("builtins.input", side_effect=["4", "Test Player 2", "6"])
    @patch("builtins.print")
    @patch.object(Game, "check_valid_user", return_value="Test Player 2")
    @patch.object(Player, "change_name")
    @patch.object(Intelligence, "change_difficulty")
    def test_user_menu_change_name(
        self,
        mock_change_difficulty,
        mock_change_name,
        mock_check_valid_user,
        mock_print,
        mock_input,
    ):
        """Test user menu change name"""
        player = Player("Test Player")
        Game.user_menu(player)
        mock_check_valid_user.assert_called_once()
        mock_change_name.assert_called_once_with("Test Player 2")
        mock_change_difficulty.assert_called_once_with("EASY")

    @patch("builtins.input", side_effect=["5", "6"])
    @patch("builtins.print")
    @patch.object(Game, "rules")
    @patch.object(Intelligence, "change_difficulty")
    def test_user_menu_rules(
        self, mock_change_difficulty, mock_rules, mock_print, mock_input
    ):
        """Test user menu rules"""
        player = Player("Test Player")
        Game.user_menu(player)
        mock_rules.assert_called_once()
        mock_change_difficulty.assert_called_once_with("EASY")

    @patch("builtins.input", return_value="6")
    @patch("builtins.print")
    @patch.object(Intelligence, "change_difficulty")
    def test_user_menu_sign_out(self, mock_change_difficulty, mock_print, mock_input):
        """Test user menu sign out"""
        player = Player("Test Player")
        Game.user_menu(player)
        mock_change_difficulty.assert_called_once_with("EASY")

    @patch("builtins.input", side_effect=["7", "6"])
    @patch("builtins.print")
    @patch.object(Intelligence, "change_difficulty")
    def test_user_menu_invalid_input(
        self, mock_change_difficulty, mock_print, mock_input
    ):
        """Test user menu invalid input"""
        player = Player("Test Player")
        Game.user_menu(player)
        mock_change_difficulty.assert_called_once_with("EASY")

    @patch("builtins.input", return_value="Test Player")
    @patch("builtins.print")
    @patch.object(Players, "get_players", return_value=[Player("Test Player")])
    @patch.object(Game, "user_menu")
    def test_login_valid_user(
        self, mock_user_menu, mock_get_players, mock_print, mock_input
    ):
        """Test lognin valid user"""
        Game.login()
        mock_user_menu.assert_called_once()

    @patch("builtins.input", side_effect=["Invalid User", "Test Player"])
    @patch("builtins.print")
    @patch.object(Players, "get_players", return_value=[Player("Test Player")])
    @patch.object(Game, "user_menu")
    def test_login_invalid_user(
        self, mock_user_menu, mock_get_players, mock_print, mock_input
    ):
        """Test lognin invalid user"""
        Game.login()
        mock_user_menu.assert_called_once()

    @patch("builtins.input", side_effect=["VeryLongUsername", "Test Player"])
    @patch("builtins.print")
    @patch.object(Players, "get_players", return_value=[Player("Test Player")])
    @patch.object(Game, "user_menu")
    def test_login_long_user_name(
        self, mock_user_menu, mock_get_players, mock_print, mock_input
    ):
        """Test lognin long username"""
        Game.login()
        mock_user_menu.assert_called_once()

    @patch("builtins.input", side_effect=[" ", "Test Player"])
    @patch("builtins.print")
    @patch.object(Players, "get_players", return_value=[Player("Test Player")])
    @patch.object(Game, "user_menu")
    def test_login_blank_user(
        self, mock_user_menu, mock_get_players, mock_print, mock_input
    ):
        """Test lognin blank username"""
        Game.login()
        mock_user_menu.assert_called_once()

    @patch("builtins.input", return_value="TestPlayer")
    @patch("builtins.print")
    @patch.object(Game, "check_valid_user", return_value="TestPlayer")
    @patch.object(Players, "add_player")
    @patch.object(Game, "user_menu")
    def test_create_user(
        self,
        mock_user_menu,
        mock_add_player,
        mock_check_valid_user,
        mock_print,
        mock_input,
    ):
        """Test create user"""
        Game.create_user()
        mock_check_valid_user.assert_called_once()
        mock_add_player.assert_called_once()
        mock_user_menu.assert_called_once()

    @patch("builtins.input", side_effect=["1", "3"])
    @patch("builtins.print")
    @patch.object(Players, "load_players")
    @patch.object(Game, "login")
    @patch.object(Players, "save_players")
    def test_login_menu_sign_in_then_exit(
        self, mock_save_players, mock_login, mock_load_players, mock_print, mock_input
    ):
        """Test login menu sign and then exit"""
        Game.login_menu()
        mock_login.assert_called_once()
        mock_save_players.assert_called_once()

    @patch("builtins.input", side_effect=["2", "3"])
    @patch("builtins.print")
    @patch.object(Players, "load_players")
    @patch.object(Game, "create_user")
    @patch.object(Players, "save_players")
    def test_login_menu_create_user_then_exit(
        self,
        mock_save_players,
        mock_create_user,
        mock_load_players,
        mock_print,
        mock_input,
    ):
        """Test login menu create user then exit"""
        Game.login_menu()
        mock_create_user.assert_called_once()
        mock_save_players.assert_called_once()

    @patch("builtins.input", return_value="3")
    @patch("builtins.print")
    @patch.object(Players, "load_players")
    @patch.object(Players, "save_players")
    def test_login_menu_exit_game(
        self, mock_save_players, mock_load_players, mock_print, mock_input
    ):
        """Test login menu exit"""
        Game.login_menu()
        mock_save_players.assert_called_once()

    @patch("builtins.input", side_effect=["4", "3"])
    @patch("builtins.print")
    @patch.object(Players, "load_players")
    @patch.object(Players, "save_players")
    def test_login_menu_invalid_choice_then_exit(
        self, mock_save_players, mock_load_players, mock_print, mock_input
    ):
        """Test login menu invalid choice then exit"""
        Game.login_menu()
        mock_save_players.assert_called_once()

    @patch.object(Player, "reset_game_total")
    @patch.object(Player, "reset_round_total")
    @patch.object(Intelligence, "reset_game_total")
    @patch.object(Intelligence, "reset_round_total")
    def test_reset_game_scores(
        self,
        mock_reset_round_total_intelligence,
        mock_reset_game_total_intelligence,
        mock_reset_round_total_player,
        mock_reset_game_total_player,
    ):
        """Test reset game scores"""
        player = Player("Test Player")
        Game.reset_game_scores(player)
        mock_reset_game_total_player.assert_called_once()
        mock_reset_round_total_player.assert_called_once()
        mock_reset_game_total_intelligence.assert_called_once()
        mock_reset_round_total_intelligence.assert_called_once()

    @patch("builtins.print")
    @patch.object(Player, "get_name", return_value="TestPlayer")
    @patch.object(Player, "get_game_total", return_value=10)
    @patch.object(Player, "get_round_total", return_value=5)
    @patch.object(Intelligence, "get_difficulty_level", return_value="EASY")
    @patch.object(Intelligence, "get_game_total", return_value=8)
    @patch.object(Intelligence, "get_round_total", return_value=4)
    def test_print_scoreboard(
        self,
        mock_get_round_total_intelligence,
        mock_get_game_total_intelligence,
        mock_get_difficulty_level,
        mock_get_round_total_player,
        mock_get_game_total_player,
        mock_get_name,
        mock_print,
    ):
        """Test print scoreboard"""
        player = Player("TestPlayer")
        Game.print_scoreboard(player)
        mock_get_name.assert_called_once()
        mock_get_game_total_player.assert_called_once()
        mock_get_round_total_player.assert_called_once()
        mock_get_difficulty_level.assert_called_once()
        mock_get_game_total_intelligence.assert_called_once()
        mock_get_round_total_intelligence.assert_called_once()

    @patch("builtins.input", side_effect=["3", "1", "4"])
    @patch("builtins.print")
    @patch.object(Game, "print_scoreboard", return_value=None)
    @patch.object(Player, "get_round_total")
    @patch.object(Player, "update_round_total")
    @patch.object(Player, "add_total_game")
    @patch.object(Game, "reset_game_scores")
    def test_game_menu_toggle_cheat_roll_dice_exit(
        self,
        mock_reset_game_scores,
        mock_add_total_game,
        mock_update_round_total,
        mock_get_round_total,
        mock_print_scoreboard,
        mock_print,
        mock_input,
    ):
        """Test game menu toggle cheat roll dice exit"""
        player = Player("Test")
        Game.game_menu(player)
        mock_get_round_total.assert_called_once()
        mock_update_round_total.assert_called_once()
        mock_add_total_game.assert_called_once()
        mock_reset_game_scores.assert_called_once()

    @patch("builtins.input", side_effect=["2", "4"])
    @patch("builtins.print")
    @patch.object(Game, "print_scoreboard", return_value=None)
    @patch.object(Player, "add_round_to_game_total")
    @patch.object(Player, "reset_round_total")
    @patch.object(Player, "add_total_game")
    @patch.object(Game, "reset_game_scores")
    def test_game_menu_hold_exit(
        self,
        mock_reset_game_scores,
        mock_add_total_game,
        mock_reset_round_total,
        mock_add_round_to_game_total,
        mock_print_scoreboard,
        mock_print,
        mock_input,
    ):
        """Test game menu hold exit"""
        player = Player("Test")
        Game.game_menu(player)
        mock_add_round_to_game_total.assert_called_once()
        mock_reset_round_total.assert_called_once()
        mock_add_total_game.assert_called_once()
        mock_reset_game_scores.assert_called_once()

    @patch("builtins.input", return_value="4")
    @patch("builtins.print")
    @patch.object(Game, "print_scoreboard", return_value=None)
    @patch.object(Player, "add_total_game")
    @patch.object(Game, "reset_game_scores")
    def test_game_menu_exit(
        self,
        mock_reset_game_scores,
        mock_add_total_game,
        mock_print_scoreboard,
        mock_print,
        mock_input,
    ):
        """Test game menu exit"""
        player = Player("Test")
        Game.game_menu(player)
        mock_add_total_game.assert_called_once()
        mock_reset_game_scores.assert_called_once()

    @patch("builtins.input", return_value="2")
    @patch("builtins.print")
    @patch.object(Game, "print_scoreboard", return_value=None)
    @patch.object(Player, "get_game_total", return_value=100)
    @patch.object(Player, "add_total_game")
    @patch.object(Player, "add_win")
    @patch.object(Game, "reset_game_scores")
    def test_game_menu_player_wins(
        self,
        mock_reset_game_scores,
        mock_add_win,
        mock_add_total_game,
        mock_get_game_total,
        mock_print_scoreboard,
        mock_print,
        mock_input,
    ):
        """Test game menu player wins"""
        player = Player("Test")
        Game.game_menu(player)
        mock_add_win.assert_called_once()
        mock_add_total_game.assert_called_once()
        mock_reset_game_scores.assert_called_once()

    @patch("builtins.input", return_value="2")
    @patch("builtins.print")
    @patch.object(Game, "print_scoreboard", return_value=None)
    @patch.object(Intelligence, "get_game_total", return_value=100)
    @patch.object(Player, "add_total_game")
    @patch.object(Game, "reset_game_scores")
    def test_game_menu_computer_wins(
        self,
        mock_reset_game_scores,
        mock_add_total_game,
        mock_get_game_total,
        mock_print_scoreboard,
        mock_print,
        mock_input,
    ):
        """Test game menu computer wins"""
        player = Player("Test")
        Game.game_menu(player)
        mock_add_total_game.assert_called_once()
        mock_reset_game_scores.assert_called_once()


if __name__ == "__main__":
    unittest.main()
