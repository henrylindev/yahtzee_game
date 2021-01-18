from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import display_game_intro


class TestDisplayGameIntro(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_game_intro(self, mock_stdout):
        expected = "\nWelcome to:\n\n"\
                   "                        #     #    #    #     # ####### ####### ####### #######\n"\
                   "                        #     #    #    #     # ####### ####### ####### #######\n"\
                   "                          # #    #   #  #     #    #        #   #       #      \n"\
                   "                           #    #     # #######    #       #    #####   #####  \n"\
                   "                           #    ####### #     #    #      #     #       #      \n"\
                   "                           #    #     # #     #    #     #      #       #      \n"\
                   "                           #    #     # #     #    #    ####### ####### #######\n\n"\
                   "Yahtzee is a game that involves rolling 5 dice and trying to outscore your opponent.\n"\
                   "Earn as many points as possible by going for specific combinations and bonus points.\n"\
                   "Be strategic and may the dice roll in your favour!\n"
        display_game_intro()
        self.assertEqual(expected, mock_stdout.getvalue())
