from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import display_scorecard


class TestDisplayScorecard(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_scorecard_player_1(self, mock_stdout):
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
        current_player = "Player 1"
        expected = "\n1 - Aces : -1\n"\
                   "2 - Twos : -1\n"\
                   "3 - Threes : -1\n"\
                   "4 - Fours : -1\n"\
                   "5 - Fives : -1\n"\
                   "6 - Sixes : -1\n"\
                   "Upper Subtotal : -1\n"\
                   "Bonus : -1\n"\
                   "Upper Total : -1\n"\
                   "7 - 3 of a kind : -1\n"\
                   "8 - 4 of a kind : -1\n"\
                   "9 - Full House : -1\n"\
                   "10 - Small Straight : -1\n"\
                   "11 - Large Straight : -1\n"\
                   "12 - Yahtzee : -1\n"\
                   "13 - Chance : -1\n"\
                   "Yahtzee Bonus : 0\n"\
                   "Lower Total : -1\n"\
                   "Grand Total : -1\n"
        display_scorecard(scorecard, current_player)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_scorecard_player_2(self, mock_stdout):
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
        current_player = "Player 2"
        expected = "\n1 - Aces : -1\n"\
                   "2 - Twos : -1\n"\
                   "3 - Threes : -1\n"\
                   "4 - Fours : -1\n"\
                   "5 - Fives : -1\n"\
                   "6 - Sixes : -1\n"\
                   "Upper Subtotal : -1\n"\
                   "Bonus : -1\n"\
                   "Upper Total : -1\n"\
                   "7 - 3 of a kind : -1\n"\
                   "8 - 4 of a kind : -1\n"\
                   "9 - Full House : -1\n"\
                   "10 - Small Straight : -1\n"\
                   "11 - Large Straight : -1\n"\
                   "12 - Yahtzee : -1\n"\
                   "13 - Chance : -1\n"\
                   "Yahtzee Bonus : 0\n"\
                   "Lower Total : -1\n"\
                   "Grand Total : -1\n"
        display_scorecard(scorecard, current_player)
        self.assertEqual(expected, mock_stdout.getvalue())
