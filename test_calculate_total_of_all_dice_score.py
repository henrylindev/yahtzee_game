from unittest import TestCase

from yahtzee import calculate_total_of_all_dice_score


class TestCalculateTotalOfAllDiceScore(TestCase):

    def test_calculate_total_of_all_dice_score_3_of_a_kind(self):
        score_choice = "7 - 3 of a kind"
        held_dice = [1, 1, 1, 4, 5]
        expected = 12
        actual = calculate_total_of_all_dice_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_total_of_all_dice_score_choose_7_with_no_3_of_a_kind(self):
        score_choice = "7 - 3 of a kind"
        held_dice = [4, 4, 5, 5, 6]
        expected = 0
        actual = calculate_total_of_all_dice_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_total_of_all_dice_score_4_of_a_kind(self):
        score_choice = "8 - 4 of a kind"
        held_dice = [4, 4, 4, 4, 5]
        expected = 21
        actual = calculate_total_of_all_dice_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_total_of_all_dice_score_choose_8_with_no_4_of_a_kind(self):
        score_choice = "8 - 4 of a kind"
        held_dice = [4, 4, 5, 5, 6]
        expected = 0
        actual = calculate_total_of_all_dice_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_total_of_all_dice_score_chance(self):
        score_choice = "13 - Chance"
        held_dice = [4, 4, 4, 5, 6]
        expected = 23
        actual = calculate_total_of_all_dice_score(score_choice, held_dice)
        self.assertEqual(expected, actual)
