from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import display_rolled_dice


class TestDisplayRolledDice(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_rolled_dice_lowest_roll(self, mock_stdout):
        held_dice = [1, 1, 1, 1, 1]
        expected = '\nYou rolled the following dice: [1, 1, 1, 1, 1].\n'\
                   '⚀ ⚀ ⚀ ⚀ ⚀\n'
        display_rolled_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_rolled_dice_highest_roll(self, mock_stdout):
        held_dice = [6, 6, 6, 6, 6]
        expected = '\nYou rolled the following dice: [6, 6, 6, 6, 6].\n'\
                   '⚅ ⚅ ⚅ ⚅ ⚅\n'
        display_rolled_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())
