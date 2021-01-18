from unittest import TestCase

from yahtzee import calculate_small_straight_score


class TestCalculateSmallStraightScore(TestCase):

    def test_calculate_small_straight_score_small_straight(self):
        score_choice = "10 - Small Straight"
        held_dice = [1, 2, 3, 4, 6]
        expected = 30
        actual = calculate_small_straight_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_small_straight_score_choose_10_with_no_small_straight(self):
        score_choice = "10 - Small Straight"
        held_dice = [1, 2, 3, 5, 6]
        expected = 0
        actual = calculate_small_straight_score(score_choice, held_dice)
        self.assertEqual(expected, actual)
