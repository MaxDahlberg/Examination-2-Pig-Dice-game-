import unittest
from player import Player


class TestPlayerClass(unittest.TestCase):
    """Test init the player object."""

    def test_init_player_object(self):
        result = Player("Test_init")
        expected = Player
        self.assertIsInstance(result, expected)

    def test_change_name(self):
        """Test change the name."""
        test_player = Player("Test_name")
        test_player.change_name("Test_name_change")

        result = test_player.get_name()
        expected = "Test_name_change"

        self.assertEqual(result, expected)

    def test_update_round_total(self):
        """Test update the total round score."""
        test_player = Player("Test")
        total_before = test_player.get_round_total()
        test_player.update_round_total(20)
        total_after = test_player.get_round_total()

        self.assertEqual(total_before, 0)
        self.assertEqual(total_after, 20)

    def test_add_round_to_game_total(self):
        """Test update the total round score."""
        test_player = Player("Test")
        test_player.update_round_total(20)
        total_before = test_player.get_game_total()
        test_player.add_round_to_game_total()
        total_after = test_player.get_game_total()

        self.assertEqual(total_before, 0)
        self.assertEqual(total_after, total_before + 20)

    def test_reset_round_total(self):
        """Test reset the total round score."""
        test_player = Player("Test")
        test_player.update_round_total(20)
        total_before = test_player.get_round_total()
        test_player.reset_round_total()
        total_after = test_player.get_round_total()

        self.assertEqual(total_before, 20)
        self.assertEqual(total_after, 0)

    def test_reset_game_total(self):
        """Test reset the total game score."""
        test_player = Player("Test")
        test_player.update_round_total(20)
        test_player.add_round_to_game_total()
        total_before = test_player.get_game_total()
        test_player.reset_game_total()
        total_after = test_player.get_game_total()

        self.assertEqual(total_before, 20)
        self.assertEqual(total_after, 0)

    def test_add_total_game(self):
        """Test add 1 game to the total game score."""
        test_player = Player("Test")
        total_before = test_player.get_total_games()
        test_player.add_total_game()
        total_after = test_player.get_total_games()

        self.assertEqual(total_before, 0)
        self.assertEqual(total_after, total_before + 1)

    def test_add_win(self):
        """Test add 1 win to the total win score."""
        test_player = Player("Test")
        total_before = test_player.get_total_wins()
        test_player.add_win()
        total_after = test_player.get_total_wins()

        self.assertEqual(total_before, 0)
        self.assertEqual(total_after, total_before + 1)

    def test_get_name(self):
        """Test get name."""
        test_player = Player("Test")
        result = test_player.get_name()
        expected = "Test"

        self.assertEqual(result, expected)

    def test_get_game_total(self):
        """Test get total game score."""
        test_player = Player("Test")
        test_player.update_round_total(20)
        test_player.add_round_to_game_total()
        result = test_player.get_game_total()
        expected = 20

        self.assertEqual(result, expected)

    def test_get_round_total(self):
        """Test get total round score."""
        test_player = Player("Test")
        test_player.update_round_total(20)
        result = test_player.get_round_total()
        expected = 20

        self.assertEqual(result, expected)

    def test_get_total_games(self):
        """Test get total number of games."""
        test_player = Player("Test")
        test_player.add_total_game()
        result = test_player.get_total_games()
        expected = 1

        self.assertEqual(result, expected)

    def test_get_total_wins(self):
        """Test get total number of wins."""
        test_player = Player("Test")
        test_player.add_win()
        result = test_player.get_total_wins()
        expected = 1

        self.assertEqual(result, expected)

    def test_get_win_percent(self):
        """Test get win % if total games are not 0."""
        test_player = Player("Test")
        test_0_result = test_player.get_win_percent()
        test_0_expected = 0

        test_player.add_win()
        test_player.add_total_game()
        test_100_result = test_player.get_win_percent()
        test_100_expected = 100

        test_player.add_total_game()
        test_50_result = test_player.get_win_percent()
        test_50_expected = 50

        self.assertEqual(test_0_result, test_0_expected)
        self.assertEqual(test_100_result, test_100_expected)
        self.assertEqual(test_50_result, test_50_expected)


if __name__ == "__main__":
    unittest.main()
