from unittest import TestCase

from yahtzee import load_scorecard


class TestLoadScorecard(TestCase):

    def test_load_scorecard(self):
        expected = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                 '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                 '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                 '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                 '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1},
                    'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                 '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                 '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                 '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                 '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        actual = load_scorecard()
        self.assertEqual(expected, actual)
