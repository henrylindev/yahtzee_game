from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import update_player_choice_score
from yahtzee import display_scorecard


class TestUpdatePlayerChoiceScore(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_player_choice_score(self, mock_stdout):
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
        score_choice = "1 - Aces"
        category_score = 5
        expected = "\n1 - Aces : 5\n"\
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
        update_player_choice_score(scorecard, current_player, score_choice, category_score)
        display_scorecard(scorecard, current_player)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_player_choice_score_last_valid_choice(self, mock_stdout):
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
        score_choice = "13 - Chance"
        category_score = 20
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
                   "13 - Chance : 20\n"\
                   "Yahtzee Bonus : 0\n"\
                   "Lower Total : -1\n"\
                   "Grand Total : -1\n"
        update_player_choice_score(scorecard, current_player, score_choice, category_score)
        display_scorecard(scorecard, current_player)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_player_choice_score_yahtzee_bonus(self, mock_stdout):
        scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': 50,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': -1, 'Grand Total': -1},
                     'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        current_player = "Player 1"
        score_choice = "12 - Yahtzee"
        category_score = 100
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
                   "12 - Yahtzee : 50\n"\
                   "13 - Chance : -1\n"\
                   "Yahtzee Bonus : 200\n"\
                   "Lower Total : -1\n"\
                   "Grand Total : -1\n"
        update_player_choice_score(scorecard, current_player, score_choice, category_score)
        display_scorecard(scorecard, current_player)
        self.assertEqual(expected, mock_stdout.getvalue())
