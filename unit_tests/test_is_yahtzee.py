from unittest import TestCase

from yahtzee import is_yahtzee


class TestIsYahtzee(TestCase):

    def test_is_yahtzee_yes(self):
        held_dice = [1, 1, 1, 1, 1]
        expected = True
        actual = is_yahtzee(held_dice)
        self.assertEqual(expected, actual)

    def test_is_yahtzee_no(self):
        held_dice = [1, 1, 1, 1, 6]
        expected = False
        actual = is_yahtzee(held_dice)
        self.assertEqual(expected, actual)
