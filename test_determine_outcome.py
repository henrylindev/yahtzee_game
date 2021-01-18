from unittest import TestCase

from yahtzee import determine_outcome


class TestDetermineOutcome(TestCase):

    def test_determine_outcome_player_1_win(self):
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
        expected = "Player 1"
        actual = determine_outcome(scorecard)
        self.assertEqual(expected, actual)

    def test_determine_winner_player_2_win(self):
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
        expected = "Player 2"
        actual = determine_outcome(scorecard)
        self.assertEqual(expected, actual)

    def test_determine_winner_player_tie_game(self):
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
        expected = "Tie"
        actual = determine_outcome(scorecard)
        self.assertEqual(expected, actual)
