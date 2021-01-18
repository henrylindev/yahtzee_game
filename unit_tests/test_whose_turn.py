from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import whose_turn


class TestWhoseTurn(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_whose_turn_player_1(self, mock_input):
        scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1},
                     'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        expected = "Player 1"
        actual = whose_turn(scorecard)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_whose_turn_player_2(self, mock_input):
        scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1},
                     'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        expected = "Player 2"
        actual = whose_turn(scorecard)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3', '2'])
    def test_whose_turn_not_player_1_or_2(self, mock_input, mock_stdout):
        scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1},
                     'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        expected = "That is not a valid input or you are out of turns! Please try again.\n"
        expected_2 = "Player 2"
        actual = whose_turn(scorecard)
        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertEqual(expected_2, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '2'])
    def test_whose_turn_out_of_turns(self, mock_input, mock_stdout):
        scorecard = {'Player 1': {'1 - Aces': 0, '2 - Twos': 0, '3 - Threes': 0, '4 - Fours': 0, '5 - Fives': 0,
                                  '6 - Sixes': 0, 'Upper Subtotal': 0, 'Bonus': 0, 'Upper Total': 0,
                                  '7 - 3 of a kind': 0, '8 - 4 of a kind': 0, '9 - Full House': 0,
                                  '10 - Small Straight': 0, '11 - Large Straight': 0, '12 - Yahtzee': 0,
                                  '13 - Chance': 0, 'Yahtzee Bonus': 0, 'Lower Total': 0, 'Grand Total': 0},
                     'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        expected = "That is not a valid input or you are out of turns! Please try again.\n"
        expected_2 = "Player 2"
        actual = whose_turn(scorecard)
        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertEqual(expected_2, actual)
