from unittest import TestCase
from unittest.mock import patch

from yahtzee import roll_dice


class TestRollDice(TestCase):

    @patch('random.randint', side_effect=[3, 3, 3, 3, 4])
    def test_roll_dice(self, dice_rolls):
        held_dice = []
        expected = [3, 3, 3, 3, 4]
        actual = roll_dice(held_dice)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3, 3, 3, 4])
    def test_roll_dice_1_dice_held(self, dice_rolls):
        held_dice = [1]
        expected = [1, 3, 3, 3, 4]
        actual = roll_dice(held_dice)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3, 3, 4])
    def test_roll_dice_2_dice_held(self, dice_rolls):
        held_dice = [1, 2]
        expected = [1, 2, 3, 3, 4]
        actual = roll_dice(held_dice)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[4, 5])
    def test_roll_dice_3_dice_held(self, dice_rolls):
        held_dice = [1, 2, 3]
        expected = [1, 2, 3, 4, 5]
        actual = roll_dice(held_dice)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[6])
    def test_roll_dice_4_dice_held(self, dice_rolls):
        held_dice = [1, 2, 3, 4]
        expected = [1, 2, 3, 4, 6]
        actual = roll_dice(held_dice)
        self.assertEqual(expected, actual)

    def test_roll_dice_5_dice_held(self):
        held_dice = [1, 2, 3, 4, 6]
        expected = [1, 2, 3, 4, 6]
        actual = roll_dice(held_dice)
        self.assertEqual(expected, actual)
