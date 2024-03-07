import os
import unittest
import pickle
from players import Players


class TestPlayersClass(unittest.TestCase):
    def setUp(self):
        """Set up testing environment."""
        self.test_player = "Test Player"

    def tearDown(self):
        """Clean up after testing."""
        if os.path.exists("players.bin"):
            os.remove("players.bin")

    def test_add_player(self):
        """Test add player method."""
        Players.add_player(self.test_player)
        self.assertIn(self.test_player, Players.get_players())

    def test_save_and_load_players(self):
        """Test save players and load players methods."""
        Players.add_player(self.test_player)
        Players.save_players()
        Players.players = []
        Players.load_players()
        self.assertIn(self.test_player, Players.get_players())

    def test_no_file(self):
        """Test load players when no file exists."""
        if os.path.exists("players.bin"):
            os.remove("players.bin")
        Players.load_players()
        self.assertEqual(Players.get_players(), [])


if __name__ == "__main__":
    unittest.main()
