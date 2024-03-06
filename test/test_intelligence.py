import unittest
import io
from unittest.mock import patch
from intelligence import Intelligence

class TestIntelligenceClass(unittest.TestCase):
    def check_and_play_selected_difficulty(self):
        """Test check difficulty and play the game accordingly."""
        Intelligence.difficulty_easy = True
        Intelligence.difficulty_medium = False
        Intelligence.difficulty_hard = False
        
        Intelligence.difficulty_easy = False
        Intelligence.difficulty_medium = True
        Intelligence.difficulty_hard = False
        
        Intelligence.difficulty_easy = False
        Intelligence.difficulty_medium = False
        Intelligence.difficulty_hard = True

        Intelligence.difficulty_easy = False
        Intelligence.difficulty_medium = False
        Intelligence.difficulty_hard = False

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_play_computer_moves(self, mock_stdout):
        """Test play computers dice rolls."""
        for i in range(10):
            Intelligence.play_computer_moves()
            if Intelligence.round_total != 0:
                test_succes = True
                break
        
        self.assertTrue(test_succes)

    def test_reset_round_total(self):
        """Test reset the total round score."""
        Intelligence.round_total = 5
        total_before = Intelligence.get_round_total()
        Intelligence.reset_round_total()
        total_after = Intelligence.get_round_total()

        self.assertNotEqual(total_before, total_after)
        self.assertEqual(total_after, 0)
    
    def test_reset_game_total(self):
        """Test reset the total game score."""
        Intelligence.game_total = 5
        total_before = Intelligence.get_game_total()
        Intelligence.reset_game_total()
        total_after = Intelligence.get_game_total()

        self.assertNotEqual(total_before, total_after)
        self.assertEqual(total_after, 0)
    
    def test_change_difficulty(self):
        """Change difficulty level."""
        Intelligence.difficulty_easy = False
        Intelligence.difficulty_medium = False
        Intelligence.difficulty_hard = False
        test_no_difficulty_result = Intelligence.get_difficulty_level()
        test_no_difficulty_expected = "No difficulty selected"

        Intelligence.change_difficulty("EASY")
        test_easy_result = Intelligence.get_difficulty_level()
        test_easy_expected = "Cpu Easy"

        Intelligence.change_difficulty("MEDIUM")
        test_medium_result = Intelligence.get_difficulty_level()
        test_medium_expected = "Cpu Medium"

        Intelligence.change_difficulty("HARD")
        test_hard_result = Intelligence.get_difficulty_level()
        test_hard_expected = "Cpu Hard"

        self.assertEqual(test_no_difficulty_result, test_no_difficulty_expected)
        self.assertEqual(test_easy_result, test_easy_expected)
        self.assertEqual(test_medium_result, test_medium_expected)
        self.assertEqual(test_hard_result, test_hard_expected)

    def test_get_difficulty_level(self):
        """Test get difficulty level."""
        Intelligence.difficulty_easy = True
        Intelligence.difficulty_medium = False
        Intelligence.difficulty_hard = False
        test_easy_result = Intelligence.get_difficulty_level()
        test_easy_expected = "Cpu Easy"
        
        Intelligence.difficulty_easy = False
        Intelligence.difficulty_medium = True
        Intelligence.difficulty_hard = False
        test_medium_result = Intelligence.get_difficulty_level()
        test_medium_expected = "Cpu Medium"
        
        Intelligence.difficulty_easy = False
        Intelligence.difficulty_medium = False
        Intelligence.difficulty_hard = True
        test_hard_result = Intelligence.get_difficulty_level()
        test_hard_expected = "Cpu Hard"

        Intelligence.difficulty_easy = False
        Intelligence.difficulty_medium = False
        Intelligence.difficulty_hard = False
        test_no_difficulty_result = Intelligence.get_difficulty_level()
        test_no_difficulty_expected = "No difficulty selected"

        self.assertEqual(test_easy_result, test_easy_expected)
        self.assertEqual(test_medium_result, test_medium_expected)
        self.assertEqual(test_hard_result, test_hard_expected)
        self.assertEqual(test_no_difficulty_result, test_no_difficulty_expected)

    def test_get_round_total(self):
        """Test get total round score."""
        Intelligence.round_total = 5
        result = Intelligence.get_round_total()
        expected = 5

        self.assertEqual(result, expected)
    
    def test_get_game_total(self):
        """Test get total game score."""
        Intelligence.game_total = 5
        result = Intelligence.get_game_total()
        expected = 5

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()