from unittest import TestCase

from yahtzee import calculate_upper_score


class TestCalculateUpperScore(TestCase):

    def test_calculate_upper_score_aces(self):
        score_choice = "1 - Aces"
        held_dice = [1, 2, 3, 4, 5]
        expected = 1
        actual = calculate_upper_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_upper_score_twos(self):
        score_choice = "2 - Twos"
        held_dice = [2, 2, 3, 4, 5]
        expected = 4
        actual = calculate_upper_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_upper_score_threes(self):
        score_choice = "3 - Threes"
        held_dice = [3, 3, 3, 4, 5]
        expected = 9
        actual = calculate_upper_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_upper_score_fours(self):
        score_choice = "4 - Fours"
        held_dice = [3, 3, 4, 4, 5]
        expected = 8
        actual = calculate_upper_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_upper_score_fives(self):
        score_choice = "5 - Fives"
        held_dice = [3, 3, 4, 5, 5]
        expected = 10
        actual = calculate_upper_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_upper_score_sixes(self):
        score_choice = "6 - Sixes"
        held_dice = [6, 6, 6, 6, 6]
        expected = 30
        actual = calculate_upper_score(score_choice, held_dice)
        self.assertEqual(expected, actual)

    def test_calculate_upper_score_selected_number_not_rolled(self):
        score_choice = "6 - Sixes"
        held_dice = [3, 3, 4, 5, 5]
        expected = 0
        actual = calculate_upper_score(score_choice, held_dice)
        self.assertEqual(expected, actual)
