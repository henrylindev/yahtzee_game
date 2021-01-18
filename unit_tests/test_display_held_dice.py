from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import display_held_dice


class TestDisplayHeldDice(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_held_dice_no_dice(self, mock_stdout):
        held_dice = []
        expected = "\nYou are holding the following dice: [].\n\n"
        display_held_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_held_dice_1_dice(self, mock_stdout):
        held_dice = [1]
        expected = "\nYou are holding the following dice: [1].\n"\
                   "⚀\n"
        display_held_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_held_dice_2_dice(self, mock_stdout):
        held_dice = [1, 2]
        expected = "\nYou are holding the following dice: [1, 2].\n"\
                   "⚀ ⚁\n"
        display_held_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_held_dice_3_dice(self, mock_stdout):
        held_dice = [1, 2, 3]
        expected = "\nYou are holding the following dice: [1, 2, 3].\n"\
                   "⚀ ⚁ ⚂\n"
        display_held_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_held_dice_4_dice(self, mock_stdout):
        held_dice = [1, 2, 3, 4]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4].\n"\
                   "⚀ ⚁ ⚂ ⚃\n"
        display_held_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_held_dice_5_dice(self, mock_stdout):
        held_dice = [1, 2, 3, 4, 5]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4, 5].\n"\
                   "⚀ ⚁ ⚂ ⚃ ⚄\n"
        display_held_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())
