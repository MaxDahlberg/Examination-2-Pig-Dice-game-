import unittest
from unittest.mock import patch, MagicMock, call
from leaderboard import Leaderboard
from players import Players


class TestLeaderboardClass(unittest.TestCase):
    @patch("builtins.print")
    @patch.object(Players, "get_players")
    def test_print_leaderboard(self, mock_get_players, mock_print):
        """Test printing of leaderboard"""
        mock_player1 = MagicMock()
        mock_player1.get_name.return_value = "Player1"
        mock_player1.get_total_wins.return_value = 10
        mock_player1.get_win_percent.return_value = 50.0

        mock_player2 = MagicMock()
        mock_player2.get_name.return_value = "Player2"
        mock_player2.get_total_wins.return_value = 20
        mock_player2.get_win_percent.return_value = 66.7

        mock_get_players.return_value = [mock_player1, mock_player2]

        Leaderboard.print_leaderboard()

        expected_output = [
            call("╭───────────────────────────────╮"),
            call("│          Leaderboard          │"),
            call("│───────────────────────────────│"),
            call("│ Name           Wins    Win%   │"),
            call("│───────────────────────────────│"),
            call("│ Player2        20      66.7   │"),
            call("│ Player1        10      50.0   │"),
            call("╰───────────────────────────────╯"),
        ]

        mock_print.assert_has_calls(expected_output, any_order=False)

if __name__ == "__main__":
    unittest.main()
