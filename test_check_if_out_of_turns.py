from unittest import TestCase

from yahtzee import check_if_out_of_turns


class TestCheckIfOutOfTurns(TestCase):

    def test_check_if_out_of_turns_not_out_of_turns(self):
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
        player_number = "1"
        expected = False
        actual = check_if_out_of_turns(scorecard, player_number)
        self.assertEqual(expected, actual)

    def test_check_if_out_of_turns_out_of_turns(self):
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
        player_number = "1"
        expected = True
        actual = check_if_out_of_turns(scorecard, player_number)
        self.assertEqual(expected, actual)
