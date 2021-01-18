from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import display_dice_images


class TestDisplayDiceImages(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_dice_images_dice_face_1(self, mock_stdout):
        held_dice = [1]
        expected = "⚀\n"
        display_dice_images(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_dice_images_dice_face_2(self, mock_stdout):
        held_dice = [2]
        expected = "⚁\n"
        display_dice_images(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_dice_images_dice_face_3(self, mock_stdout):
        held_dice = [3]
        expected = "⚂\n"
        display_dice_images(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_dice_images_dice_face_4(self, mock_stdout):
        held_dice = [4]
        expected = "⚃\n"
        display_dice_images(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_dice_images_dice_face_5(self, mock_stdout):
        held_dice = [5]
        expected = "⚄\n"
        display_dice_images(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_dice_images_dice_face_6(self, mock_stdout):
        held_dice = [6]
        expected = "⚅\n"
        display_dice_images(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_dice_images_5_dice(self, mock_stdout):
        held_dice = [1, 2, 3, 4, 5]
        expected = "⚀ ⚁ ⚂ ⚃ ⚄\n"
        display_dice_images(held_dice)
        self.assertEqual(expected, mock_stdout.getvalue())
