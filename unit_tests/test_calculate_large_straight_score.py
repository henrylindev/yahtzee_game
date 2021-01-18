from unittest import TestCase

from yahtzee import calculate_large_straight_score


class TestCalculateLargeStraightScore(TestCase):

    def test_calculate_large_straight_score_large_straight(self):
        score_choice = "11 - Large Straight"
        held_dice = [1, 2, 3, 4, 5]
        expected = 40
        actual = calculate_large_straight_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_large_straight_score_choose_11_with_no_large_straight(self):
        score_choice = "11 - Large Straight"
        held_dice = [1, 2, 3, 5, 6]
        expected = 0
        actual = calculate_large_straight_score(score_choice, held_dice)
        self.assertEqual(expected, actual)
