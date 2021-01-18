from unittest import TestCase

from yahtzee import calculate_upper_bonus


class TestCalculateUpperBonus(TestCase):

    def test_calculate_upper_bonus_no_bonus(self):
        scorecard = {'Player 1': {'1 - Aces': 0, '2 - Twos': 4, '3 - Threes': 9, '4 - Fours': 12, '5 - Fives': 10,
                                  '6 - Sixes': 24, 'Upper Subtotal': 59, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1},
                     'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        current_player = "Player 1"
        expected = 0
        actual = calculate_upper_bonus(scorecard, current_player)
        self.assertEqual(expected, actual)

    def test_calculate_upper_bonus_bonus_earned(self):
        scorecard = {'Player 1': {'1 - Aces': 3, '2 - Twos': 6, '3 - Threes': 12, '4 - Fours': 16, '5 - Fives': 20,
                                  '6 - Sixes': 24, 'Upper Subtotal': 81, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1},
                     'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        current_player = "Player 1"
        expected = 35
        actual = calculate_upper_bonus(scorecard, current_player)
        self.assertEqual(expected, actual)
