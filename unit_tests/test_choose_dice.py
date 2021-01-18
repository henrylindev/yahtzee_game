from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import choose_dice


class TestChooseDice(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['0'])
    def test_choose_dice_keep_all(self, mock_input, mock_stdout):
        held_dice = [1, 2, 3, 4, 6]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n"
        expected_2 = [1, 2, 3, 4, 6]
        actual = choose_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertEqual(expected_2, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '0'])
    def test_choose_dice_remove_1(self, mock_input, mock_stdout):
        held_dice = [1, 2, 3, 4, 6]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n"\
                   "\nYou are holding the following dice: [2, 3, 4, 6].\n"
        expected_2 = [2, 3, 4, 6]
        actual = choose_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertEqual(expected_2, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '2', '0'])
    def test_choose_dice_remove_2(self, mock_input, mock_stdout):
        held_dice = [1, 2, 3, 4, 6]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n" \
                   "\nYou are holding the following dice: [2, 3, 4, 6].\n"\
                   "\nYou are holding the following dice: [3, 4, 6].\n"
        expected_2 = [3, 4, 6]
        actual = choose_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertEqual(expected_2, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '2', '3', '0'])
    def test_choose_dice_remove_3(self, mock_input, mock_stdout):
        held_dice = [1, 2, 3, 4, 6]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n" \
                   "\nYou are holding the following dice: [2, 3, 4, 6].\n"\
                   "\nYou are holding the following dice: [3, 4, 6].\n"\
                   "\nYou are holding the following dice: [4, 6].\n"
        expected_2 = [4, 6]
        actual = choose_dice(held_dice)
        self.assertEqual(expected_2, actual)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '0'])
    def test_choose_dice_remove_4(self, mock_input, mock_stdout):
        held_dice = [1, 2, 3, 4, 6]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n" \
                   "\nYou are holding the following dice: [2, 3, 4, 6].\n"\
                   "\nYou are holding the following dice: [3, 4, 6].\n"\
                   "\nYou are holding the following dice: [4, 6].\n"\
                   "\nYou are holding the following dice: [6].\n"
        expected_2 = [6]
        actual = choose_dice(held_dice)
        self.assertEqual(expected_2, actual)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '6', '0'])
    def test_choose_dice_remove_all(self, mock_input, mock_stdout):
        held_dice = [1, 2, 3, 4, 6]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n" \
                   "\nYou are holding the following dice: [2, 3, 4, 6].\n"\
                   "\nYou are holding the following dice: [3, 4, 6].\n"\
                   "\nYou are holding the following dice: [4, 6].\n"\
                   "\nYou are holding the following dice: [6].\n"\
                   "\nYou are holding the following dice: [].\n"
        expected_2 = []
        actual = choose_dice(held_dice)
        self.assertEqual(expected_2, actual)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['5', 'Hi', '0'])
    def test_choose_dice_invalid_choice(self, mock_input, mock_stdout):
        held_dice = [1, 2, 3, 4, 6]
        expected = "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n"\
                   "None of your dice have that value! Please try again.\n"\
                   "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n"\
                   "None of your dice have that value! Please try again.\n"\
                   "\nYou are holding the following dice: [1, 2, 3, 4, 6].\n"
        expected_2 = [1, 2, 3, 4, 6]
        actual = choose_dice(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertEqual(expected_2, actual)
