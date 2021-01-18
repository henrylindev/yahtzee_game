from unittest import TestCase

from yahtzee import is_the_game_not_over


class TestIsTheGameNotOver(TestCase):

    def test_is_the_game_not_over_game_over(self):
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
        expected = False
        actual = is_the_game_not_over(scorecard)
        self.assertEqual(expected, actual)

    def test_is_the_game_not_over_game_not_over(self):
        scorecard = {'Player 1': {'1 - Aces': 0, '2 - Twos': 4, '3 - Threes': 9, '4 - Fours': 12, '5 - Fives': 10,
                                  '6 - Sixes': 24, 'Upper Subtotal': 59, 'Bonus': 0, 'Upper Total': 59,
                                  '7 - 3 of a kind': 20, '8 - 4 of a kind': 20, '9 - Full House': 25,
                                  '10 - Small Straight': 30, '11 - Large Straight': 40, '12 - Yahtzee': 50,
                                  '13 - Chance': 25, 'Yahtzee Bonus': 0, 'Lower Total': 210, 'Grand Total': 269},
                     'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1,
                                  '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1,
                                  '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1,
                                  '10 - Small Straight': -1, '11 - Large Straight': -1, '12 - Yahtzee': -1,
                                  '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
        expected = True
        actual = is_the_game_not_over(scorecard)
        self.assertEqual(expected, actual)
