import unittest
import io
from unittest.mock import patch
from dice import Dice

class TestDiceClass(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_roll_dice(self, mock_stdout):
        """Testing rolling of dice with and without cheat enabled"""
        for i in range(100):
            Dice.roll_dice(0 , True)
            expected_outputs = [Dice.face_2() + "\n", Dice.face_3() + "\n", Dice.face_4() + "\n", Dice.face_5() + "\n", Dice.face_6() + "\n"]
            self.assertIn(mock_stdout.getvalue(), expected_outputs)
            mock_stdout.seek(0)
            mock_stdout.truncate(0)

        for i in range(100):
            round_total = Dice.roll_dice(0 , True)
            output = mock_stdout.getvalue()

            if output == Dice.face_2() + "\n":
                if round_total == 2:
                    correct_round_total = True
            
            if output == Dice.face_3() + "\n":
                if round_total == 3:
                    correct_round_total = True
            
            if output == Dice.face_4() + "\n":
                if round_total == 4:
                    correct_round_total = True
            
            if output == Dice.face_5() + "\n":
                if round_total == 5:
                    correct_round_total = True
            
            if output == Dice.face_6() + "\n":
                if round_total == 6:
                    correct_round_total = True
            
            self.assertTrue(correct_round_total)
            mock_stdout.seek(0)
            mock_stdout.truncate(0) 

        for i in range(100):
            round_total = Dice.roll_dice(0 , False)
            output = mock_stdout.getvalue()
            if output == Dice.face_1() + "\n        ╭───────────────╮\n        │   Rolled  1   │\n        ╰───────────────╯\n\n":
                if round_total == 0:
                    correct_round_total = True

            self.assertTrue(correct_round_total)
            mock_stdout.seek(0)
            mock_stdout.truncate(0) 
            break

    def test_face_1(self):
        """Test get dice face 1."""
        result = Dice.face_1()
        expected = """           ╭─────────╮
           │         │
           │    ●    │
           │         │
           ╰─────────╯
"""
        self.assertEqual(result, expected)

    def test_face_2(self):
        """Test get dice face 2."""
        result = Dice.face_2()
        expected = """           ╭─────────╮
           │  ●      │
           │         │
           │      ●  │
           ╰─────────╯
"""
        self.assertEqual(result, expected)

    def test_face_3(self):
        """Test get dice face 3."""
        result = Dice.face_3()
        expected = """           ╭─────────╮
           │  ●      │
           │    ●    │
           │      ●  │
           ╰─────────╯
"""
        self.assertEqual(result, expected)

    def test_face_4(self):
        """Test get dice face 4."""
        result = Dice.face_4()
        expected = """           ╭─────────╮
           │  ●   ●  │
           │         │
           │  ●   ●  │
           ╰─────────╯
"""
        self.assertEqual(result, expected)

    def test_face_5(self):
        """Test get dice face 5."""
        result = Dice.face_5()
        expected = """           ╭─────────╮
           │  ●   ●  │
           │    ●    │
           │  ●   ●  │
           ╰─────────╯
"""
        self.assertEqual(result, expected)

    def test_face_6(self):
        """Test get dice face 6."""
        result = Dice.face_6()
        expected = """           ╭─────────╮
           │  ●   ●  │
           │  ●   ●  │
           │  ●   ●  │
           ╰─────────╯
"""
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()