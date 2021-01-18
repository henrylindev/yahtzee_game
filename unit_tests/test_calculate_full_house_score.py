from unittest import TestCase

from yahtzee import calculate_full_house_score


class TestCalculateFullHouseScore(TestCase):

    def test_calculate_full_house_score_3_of_a_kind_first(self):
        score_choice = "9 - Full House"
        held_dice = [1, 1, 1, 2, 2]
        expected = 25
        actual = calculate_full_house_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_full_house_score_pair_first(self):
        score_choice = "9 - Full House"
        held_dice = [1, 1, 2, 2, 2]
        expected = 25
        actual = calculate_full_house_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_full_house_score_choose_9_with_no_full_house(self):
        score_choice = "9 - Full House"
        held_dice = [1, 1, 2, 2, 3]
        expected = 0
        actual = calculate_full_house_score(score_choice, held_dice)
        self.assertEqual(expected, actual)
