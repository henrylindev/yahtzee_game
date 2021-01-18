from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import print_dice_choice_error


class TestPrintDiceChoiceError(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dice_choice_error(self, mock_stdout):
        expected = "None of your dice have that value! Please try again.\n"
        print_dice_choice_error()
        self.assertEqual(expected, mock_stdout.getvalue())
