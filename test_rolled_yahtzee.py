from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import rolled_yahtzee


class TestRolledYahtzee(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rolled_yahtzee(self, mock_stdout):
        expected = "YAHTZEE!!!\n"
        rolled_yahtzee()
        self.assertEqual(expected, mock_stdout.getvalue())
