from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import display_outcome


class TestDisplayOutcome(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_outcome_player_1_win(self, mock_stdout):
        scorecard = {'Player 1': {'1 - Aces': 0, '2 - Twos': 4, '3 - Threes': 9, '4 - Fours': 12, '5 - Fives': 10,
                                  '6 - Sixes': 24, 'Upper Subtotal': 59, 'Bonus': 0, 'Upper Total': 59,
                                  '7 - 3 of a kind': 20, '8 - 4 of a kind': 20, '9 - Full House': 25,
                                  '10 - Small Straight': 30, '11 - Large Straight': 40, '12 - Yahtzee': 50,
                                  '13 - Chance': 25, 'Yahtzee Bonus': 0, 'Lower Total': 210, 'Grand Total': 269},
                     'Player 2': {'1 - Aces': 0, '2 - Twos': 0, '3 - Threes': 0, '4 - Fours': 0, '5 - Fives': 0,
                                  '6 - Sixes': 0, 'Upper Subtotal': 0, 'Bonus': 0, 'Upper Total': 0,
                                  '7 - 3 of a kind': 0, '8 - 4 of a kind': 0, '9 - Full House': 0,
                                  '10 - Small Straight': 0, '11 - Large Straight': 0, '12 - Yahtzee': 0,
                                  '13 - Chance': 0, 'Yahtzee Bonus': 0, 'Lower Total': 0, 'Grand Total': 0}}
        outcome = "Player 1"
        expected = "\nPlayer 1 scored 269 points and Player 2 scored 0 points.\n" \
                   "Congratulations Player 1! You win!!!\n"
        display_outcome(scorecard, outcome)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_outcome_player_2_win(self, mock_stdout):
        scorecard = {'Player 1': {'1 - Aces': 0, '2 - Twos': 0, '3 - Threes': 0, '4 - Fours': 0, '5 - Fives': 0,
                                  '6 - Sixes': 0, 'Upper Subtotal': 0, 'Bonus': 0, 'Upper Total': 0,
                                  '7 - 3 of a kind': 0, '8 - 4 of a kind': 0, '9 - Full House': 0,
                                  '10 - Small Straight': 0, '11 - Large Straight': 0, '12 - Yahtzee': 0,
                                  '13 - Chance': 0, 'Yahtzee Bonus': 0, 'Lower Total': 0, 'Grand Total': 0},
                     'Player 2': {'1 - Aces': 0, '2 - Twos': 4, '3 - Threes': 9, '4 - Fours': 12, '5 - Fives': 10,
                                  '6 - Sixes': 24, 'Upper Subtotal': 59, 'Bonus': 0, 'Upper Total': 59,
                                  '7 - 3 of a kind': 20, '8 - 4 of a kind': 20, '9 - Full House': 25,
                                  '10 - Small Straight': 30, '11 - Large Straight': 40, '12 - Yahtzee': 50,
                                  '13 - Chance': 25, 'Yahtzee Bonus': 0, 'Lower Total': 210, 'Grand Total': 269}}
        outcome = "Player 2"
        expected = "\nPlayer 1 scored 0 points and Player 2 scored 269 points.\n" \
                   "Congratulations Player 2! You win!!!\n"
        display_outcome(scorecard, outcome)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_outcome_tie_game(self, mock_stdout):
        scorecard = {'Player 1': {'1 - Aces': 0, '2 - Twos': 4, '3 - Threes': 9, '4 - Fours': 12, '5 - Fives': 10,
                                  '6 - Sixes': 24, 'Upper Subtotal': 59, 'Bonus': 0, 'Upper Total': 59,
                                  '7 - 3 of a kind': 20, '8 - 4 of a kind': 20, '9 - Full House': 25,
                                  '10 - Small Straight': 30, '11 - Large Straight': 40, '12 - Yahtzee': 50,
                                  '13 - Chance': 25, 'Yahtzee Bonus': 0, 'Lower Total': 210, 'Grand Total': 269},
                     'Player 2': {'1 - Aces': 0, '2 - Twos': 4, '3 - Threes': 9, '4 - Fours': 12, '5 - Fives': 10,
                                  '6 - Sixes': 24, 'Upper Subtotal': 59, 'Bonus': 0, 'Upper Total': 59,
                                  '7 - 3 of a kind': 20, '8 - 4 of a kind': 20, '9 - Full House': 25,
                                  '10 - Small Straight': 30, '11 - Large Straight': 40, '12 - Yahtzee': 50,
                                  '13 - Chance': 25, 'Yahtzee Bonus': 0, 'Lower Total': 210, 'Grand Total': 269}}
        outcome = "Tie"
        expected = "\nPlayer 1 scored 269 points and Player 2 scored 269 points.\n" \
                   "Wow! What are the odds? Tie game!\n"
        display_outcome(scorecard, outcome)
        self.assertEqual(expected, mock_stdout.getvalue())
