"""
COMP 1510 Final Exam
Yahtzee!
Henry Lin
"""
import doctest
import json
import random
import re


def YAHTZEE_BONUS_SCORE() -> int:
    """
    Return 100 points for the Yahtzee bonus score.
    """
    return 100


def UPPER_BONUS_THRESHOLD() -> int:
    """
    Return 62 points for the threshold required to get the upper bonus points.
    """
    return 62


def YAHTZEE_SCORE() -> int:
    """
    Return 50 points for the Yahtzee score.
    """
    return 50


def LARGE_STRAIGHT_SCORE() -> int:
    """
    Return 40 points for the large straight score.
    """
    return 40


def UPPER_BONUS_SCORE() -> int:
    """
    Return 35 points for the upper bonus score.
    """
    return 35


def SMALL_STRAIGHT_SCORE() -> int:
    """
    Return 30 points for the small straight score.
    """
    return 30


def FULL_HOUSE_SCORE() -> int:
    """
    Return 25 points for the full house score.
    """
    return 25


def SIXES_SCORE() -> int:
    """
    Return 6 points for the sixes score.
    """
    return 6


def FIVES_SCORE() -> int:
    """
    Return 5 points for the fives score.
    """
    return 5


def FOURS_SCORE() -> int:
    """
    Return 4 points for the fours score.
    """
    return 4


def THREES_SCORE() -> int:
    """
    Return 3 points for the threes score.
    """
    return 3


def TWOS_SCORE() -> int:
    """
    Return 2 points for the twos score.
    """
    return 2


def ACES_SCORE() -> int:
    """
    Return 1 point for the aces score.
    """
    return 1


def DEFAULT_SCORE() -> int:
    """
    Return 0 points for the default score.
    """
    return 0


def NO_SCORE() -> int:
    """
    Return -1 points for no score in the category.
    """
    return -1


def display_outcome(scorecard: dict, outcome: str):
    """
    Display the outcome of the game.

    A function that prints how many points each player scored and the outcome of the game.

    :param scorecard: a non-empty dictionary of the scorecards
    :param outcome: a string representing the outcome of the game
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: outcome must be "Player 1", "Player 2", or "Tie"
    :postcondition: prints the correct outcome of the game

    >>> doc_scorecard = {'Player 1': {'1 - Aces': 5, '2 - Twos': 2, '3 - Threes': 3, '4 - Fours': 4, \
    '5 - Fives': 5, '6 - Sixes': 6, 'Upper Subtotal': 21, 'Bonus': 0, 'Upper Total': 21, \
    '7 - 3 of a kind': 0, '8 - 4 of a kind': 20, '9 - Full House': 25, '10 - Small Straight': 0, \
    '11 - Large Straight': 40, '12 - Yahtzee': 50, '13 - Chance': 20, 'Yahtzee Bonus': 100, \
    'Lower Total': 255, 'Grand Total': 276}, 'Player 2': {'1 - Aces': 0, '2 - Twos': 8, '3 - Threes': 12, \
    '4 - Fours': 16, '5 - Fives': 20, '6 - Sixes': 24, 'Upper Subtotal': 80, 'Bonus': 35, \
    'Upper Total': 115, '7 - 3 of a kind': 15, '8 - 4 of a kind': 0, '9 - Full House': 25, \
    '10 - Small Straight': 30, '11 - Large Straight': 0, '12 - Yahtzee': 0, '13 - Chance': 25, \
    'Yahtzee Bonus': 0, 'Lower Total': 95, 'Grand Total': 210}}
    >>> doc_outcome = "Player 1"
    >>> display_outcome(doc_scorecard, doc_outcome) # doctest: +NORMALIZE_WHITESPACE
    Player 1 scored 276 points and Player 2 scored 210 points.
    Congratulations Player 1! You win!!!
    """
    player_1_score = scorecard["Player 1"]["Grand Total"]
    player_2_score = scorecard["Player 2"]["Grand Total"]

    print(f"\nPlayer 1 scored {player_1_score} points and Player 2 scored {player_2_score} points.")

    if outcome == "Player 1":
        print(f"Congratulations Player 1! You win!!!")
    elif outcome == "Player 2":
        print(f"Congratulations Player 2! You win!!!")
    elif outcome == "Tie":
        print(f"Wow! What are the odds? Tie game!")


def determine_outcome(scorecard: dict) -> str:
    """
    Determine the outcome of the game.

    A function that compares both players' total scores returns the outcome of the game.

    :param scorecard: a non-empty dictionary of the scorecards
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :postcondition: returns the correct outcome of the game
    :return: outcome

    >>> doc_scorecard = {'Player 1': {'1 - Aces': 5, '2 - Twos': 2, '3 - Threes': 3, '4 - Fours': 4, \
    '5 - Fives': 5, '6 - Sixes': 6, 'Upper Subtotal': 21, 'Bonus': 0, 'Upper Total': 21, \
    '7 - 3 of a kind': 0, '8 - 4 of a kind': 20, '9 - Full House': 25, '10 - Small Straight': 0, \
    '11 - Large Straight': 40, '12 - Yahtzee': 50, '13 - Chance': 20, 'Yahtzee Bonus': 100, \
    'Lower Total': 255, 'Grand Total': 276}, 'Player 2': {'1 - Aces': 0, '2 - Twos': 8, '3 - Threes': 12, \
    '4 - Fours': 16, '5 - Fives': 20, '6 - Sixes': 24, 'Upper Subtotal': 80, 'Bonus': 35, \
    'Upper Total': 115, '7 - 3 of a kind': 15, '8 - 4 of a kind': 0, '9 - Full House': 25, \
    '10 - Small Straight': 30, '11 - Large Straight': 0, '12 - Yahtzee': 0, '13 - Chance': 25, \
    'Yahtzee Bonus': 0, 'Lower Total': 95, 'Grand Total': 210}}
    >>> determine_outcome(doc_scorecard) # doctest: +NORMALIZE_WHITESPACE
    'Player 1'
    """
    player_1_score = scorecard["Player 1"]["Grand Total"]
    player_2_score = scorecard["Player 2"]["Grand Total"]

    if player_1_score > player_2_score:
        return "Player 1"
    elif player_2_score > player_1_score:
        return "Player 2"
    else:
        return "Tie"


def is_the_game_not_over(scorecard: dict) -> bool:
    """
    Check if the game is over.

    A function that checks if both player's scorecards have any categories with -1 left and returns a Boolean value
    depending on the result.

    :param scorecard: a non-empty dictionary of the scorecards
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :postcondition: returns the correct answer to the question "is the game not over?"
    :return: Boolean value

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': 20, '6 - Sixes': -1, 'Upper Subtotal': 20, 'Bonus': 0, 'Upper Total': 20, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': 150, \
    'Grand Total': 170}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> is_the_game_not_over(doc_scorecard) # doctest: +NORMALIZE_WHITESPACE
    True
    """
    for value in scorecard["Player 1"].values():
        if value == NO_SCORE():
            return True

    for value in scorecard["Player 2"].values():
        if value == NO_SCORE():
            return True

    return False


def calculate_grand_total(scorecard: dict, current_player: str) -> int:
    """
    Calculate the "Grand Total" score.

    A function that calculates the "Grand Total" score and returns the result.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :postcondition: returns the correct score
    :return: calculated "Grand Total" score

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': 20, '6 - Sixes': -1, 'Upper Subtotal': 20, 'Bonus': 0, 'Upper Total': 20, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': 150, \
    'Grand Total': 150}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> calculate_grand_total(doc_scorecard, doc_player) # doctest: +NORMALIZE_WHITESPACE
    170
    """
    grand_total = DEFAULT_SCORE()
    total_keys = ("Upper Total", "Lower Total")
    section_totals = {key: scorecard[current_player][key] for key in total_keys}

    for value in section_totals.values():
        grand_total += value

    return grand_total


def calculate_lower_total(scorecard: dict, current_player: str) -> int:
    """
    Calculate the "Lower Total" score.

    A function that calculates the "Lower Total" score and returns the result.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :postcondition: returns the correct score
    :return: calculated "Lower Total" score

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': 20, '6 - Sixes': -1, 'Upper Subtotal': 20, 'Bonus': 0, 'Upper Total': 20, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': 150, \
    'Grand Total': 150}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> calculate_lower_total(doc_scorecard, doc_player) # doctest: +NORMALIZE_WHITESPACE
    150
    """
    lower_total = DEFAULT_SCORE()
    lower_keys = ("7 - 3 of a kind", "8 - 4 of a kind", "9 - Full House", "10 - Small Straight", "11 - Large Straight",
                  "12 - Yahtzee", "13 - Chance", "Yahtzee Bonus")
    lower_section = {key: scorecard[current_player][key] for key in lower_keys}

    for value in lower_section.values():
        if value != NO_SCORE():
            lower_total += value

    return lower_total


def calculate_upper_total(scorecard: dict, current_player: str) -> int:
    """
    Calculate the "Upper Total" score.

    A function that calculates the "Upper Total" score and returns the result.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :postcondition: returns the correct score
    :return: calculated "Upper Total" score

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': 20, '6 - Sixes': -1, 'Upper Subtotal': 20, 'Bonus': 0, 'Upper Total': 0, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': 150, \
    'Grand Total': 150}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> calculate_upper_total(doc_scorecard, doc_player) # doctest: +NORMALIZE_WHITESPACE
    20
    """
    upper_total = DEFAULT_SCORE()
    upper_total_keys = ("Upper Subtotal", "Bonus")
    upper_subtotals = {key: scorecard[current_player][key] for key in upper_total_keys}

    for value in upper_subtotals.values():
        upper_total += value

    return upper_total


def calculate_upper_bonus(scorecard: dict, current_player: str) -> int:
    """
    Calculate the "Bonus" score.

    A function that calculates the "Bonus" score and returns the result.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :postcondition: returns the correct score
    :return: calculated "Bonus" score

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': 20, '6 - Sixes': -1, 'Upper Subtotal': 20, 'Bonus': 0, 'Upper Total': 0, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': 150, \
    'Grand Total': 150}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> calculate_upper_bonus(doc_scorecard, doc_player) # doctest: +NORMALIZE_WHITESPACE
    0
    """
    if scorecard[current_player]["Upper Subtotal"] > UPPER_BONUS_THRESHOLD():
        return UPPER_BONUS_SCORE()
    else:
        return DEFAULT_SCORE()


def calculate_upper_subtotal(scorecard: dict, current_player: str) -> int:
    """
    Calculate the "Upper Subtotal" score.

    A function that calculates the "Upper Subtotal" score and returns the result.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :postcondition: returns the correct score
    :return: calculated "Upper Subtotal" score

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': 20, '6 - Sixes': -1, 'Upper Subtotal': 0, 'Bonus': 0, 'Upper Total': 0, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': 150, \
    'Grand Total': 150}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> calculate_upper_subtotal(doc_scorecard, doc_player) # doctest: +NORMALIZE_WHITESPACE
    20
    """
    upper_subtotal = DEFAULT_SCORE()
    upper_keys = ("1 - Aces", "2 - Twos", "3 - Threes", "4 - Fours", "5 - Fives", "6 - Sixes")
    upper_section = {key: scorecard[current_player][key] for key in upper_keys}

    for value in upper_section.values():
        if value != NO_SCORE():
            upper_subtotal += value

    return upper_subtotal


def update_category_score(scorecard: dict, current_player: str, key: str, value: int):
    """
    Update a category score.

    A function that updates a specific scorecard category (key) with a specific score (value).

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :param key: a string of the desired scorecard category
    :param value: an integer of the desired score
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :precondition: key must be a string of a key that exists in the scorecard dictionary
    :precondition: value must be an integer
    :postcondition: updates the correct category with the correct score

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': 20, '6 - Sixes': -1, 'Upper Subtotal': 0, 'Bonus': 0, 'Upper Total': 0, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': 150, \
    'Grand Total': 150}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> doc_key = "Upper Subtotal"
    >>> doc_value = 20
    >>> update_category_score(doc_scorecard, doc_player, doc_key, doc_value) # doctest: +NORMALIZE_WHITESPACE
    """
    scorecard[current_player][key] = value


def update_totals(scorecard: dict, current_player: str):
    """
    Update the "Bonus" and total categories.

    A function that calculates and updates the upper bonus and total categories on the scorecard.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :postcondition: updates the "Bonus" and total categories with the correct scores

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': 0, 'Upper Total': 0, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 100, 'Lower Total': 50, \
    'Grand Total': 50}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> update_totals(doc_scorecard, doc_player) # doctest: +NORMALIZE_WHITESPACE
    """
    upper_subtotal = calculate_upper_subtotal(scorecard, current_player)
    update_category_score(scorecard, current_player, "Upper Subtotal", upper_subtotal)

    upper_bonus = calculate_upper_bonus(scorecard, current_player)
    update_category_score(scorecard, current_player, "Bonus", upper_bonus)

    upper_total = calculate_upper_total(scorecard, current_player)
    update_category_score(scorecard, current_player, "Upper Total", upper_total)

    lower_total = calculate_lower_total(scorecard, current_player)
    update_category_score(scorecard, current_player, "Lower Total", lower_total)

    grand_total = calculate_grand_total(scorecard, current_player)
    update_category_score(scorecard, current_player, "Grand Total", grand_total)


def update_player_choice_score(scorecard: dict, current_player: str, score_choice: str, category_score: int):
    """
    Update the player's selected category.

    A function that updates the score of the player's selected category or the "Yahtzee Bonus" category if the player
    has already gotten one Yahtzee.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :param score_choice: a string of the category name
    :param category_score: an integer of the calculated category score
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :precondition: score_choice must be a string of a numbered category found on the scorecard
    :precondition: category_score must be an integer
    :postcondition: updates the correct category of the scorecard

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': 0, 'Bonus': 0, 'Upper Total': 0, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': 50, \
    'Grand Total': 50}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> doc_choice = "12 - Yahtzee"
    >>> doc_score = 100
    >>> update_player_choice_score(doc_scorecard, doc_player, doc_choice, doc_score) # doctest: +NORMALIZE_WHITESPACE
    """
    if score_choice == "12 - Yahtzee" and scorecard[current_player]["12 - Yahtzee"] == YAHTZEE_SCORE():
        yahtzee_bonus = scorecard[current_player]["Yahtzee Bonus"]
        yahtzee_bonus += category_score
        scorecard[current_player]["Yahtzee Bonus"] = yahtzee_bonus
    else:
        scorecard[current_player][score_choice] = category_score


def update_scorecard(scorecard: dict, current_player: str, score_choice: str, category_score: int):
    """
    Update the scorecard.

    A function that adds the calculated score to the scorecard, calculates the current totals, adds the totals to the
    scorecard, and displays the results.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :param score_choice: a string of the category name
    :param category_score: an integer of the calculated category score
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :precondition: score_choice must be a string of a numbered category found on the scorecard
    :precondition: category_score must be an integer
    :postcondition: prints the correct scorecard

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': 0, 'Bonus': 0, 'Upper Total': 0, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': 50, \
    'Grand Total': 50}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> doc_choice = "12 - Yahtzee"
    >>> doc_score = 100
    >>> update_scorecard(doc_scorecard, doc_player, doc_choice, doc_score) # doctest: +NORMALIZE_WHITESPACE
    1 - Aces : -1
    2 - Twos : -1
    3 - Threes : -1
    4 - Fours : -1
    5 - Fives : -1
    6 - Sixes : -1
    Upper Subtotal : 0
    Bonus : 0
    Upper Total : 0
    7 - 3 of a kind : -1
    8 - 4 of a kind : -1
    9 - Full House : -1
    10 - Small Straight : -1
    11 - Large Straight : -1
    12 - Yahtzee : 50
    13 - Chance : -1
    Yahtzee Bonus : 100
    Lower Total : 150
    Grand Total : 150
    """
    update_player_choice_score(scorecard, current_player, score_choice, category_score)
    update_totals(scorecard, current_player)
    display_scorecard(scorecard, current_player)


def calculate_yahtzee_score(scorecard: dict, current_player: str, held_dice: list) -> int:
    """
    Calculate the Yahtzee score.

    A function that calculates the score for the Yahtzee category and returns the result.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :param held_dice: a list of the held dice
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :precondition: held_dice must be a list
    :postcondition: returns the correct score
    :return: calculated Yahtzee score

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': 0, 'Bonus': 0, 'Upper Total': 0, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': 50, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': 50, \
    'Grand Total': 50}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> doc_held_dice = [6, 6, 6, 6, 6]
    >>> calculate_yahtzee_score(doc_scorecard, doc_player, doc_held_dice)
    100
    """
    if is_yahtzee(held_dice):
        if scorecard[current_player]["12 - Yahtzee"] == NO_SCORE():
            return YAHTZEE_SCORE()
        elif scorecard[current_player]["12 - Yahtzee"] == YAHTZEE_SCORE():
            return YAHTZEE_BONUS_SCORE()
    else:
        return DEFAULT_SCORE()


def calculate_large_straight_score(score_choice: str, held_dice: list) -> int:
    """
    Calculate the special dice score.

    A function that calculates the score of a category that requires all 5 dice to be in sequential order and returns
    the result.

    :param score_choice: a string of the category name
    :param held_dice: a list of the held dice
    :precondition: score_choice must be a string of a numbered category found on the scorecard
    :precondition: held_dice must be a list
    :postcondition: returns the correct score
    :return: calculated large straight score

    >>> doc_score_choice = "11 - Large Straight"
    >>> doc_held_dice = [1, 2, 3, 4, 6]
    >>> calculate_large_straight_score(doc_score_choice, doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    0
    """
    held_dice_as_strings = [str(dice) for dice in held_dice]
    joined_held_dice = "".join(held_dice_as_strings)

    if score_choice == "11 - Large Straight":
        if re.match(r"12345|23456", joined_held_dice):
            return LARGE_STRAIGHT_SCORE()
        else:
            return DEFAULT_SCORE()


def calculate_small_straight_score(score_choice: str, held_dice: list) -> int:
    """
    Calculate the small straight score.

    A function that calculates the score of a category that requires at least 4 dice in sequential order and returns the
    result.

    :param score_choice: a string of the category name
    :param held_dice: a list of the held dice
    :precondition: score_choice must be a string of a numbered category found on the scorecard
    :precondition: held_dice must be a list
    :postcondition: returns the correct score
    :return: calculated small straight score

    >>> doc_score_choice = "10 - Small Straight"
    >>> doc_held_dice = [1, 2, 3, 4, 6]
    >>> calculate_small_straight_score(doc_score_choice, doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    30
    """
    held_dice_as_strings = [str(dice) for dice in held_dice]
    joined_held_dice = "".join(held_dice_as_strings)

    if score_choice == "10 - Small Straight":
        if re.match(r"1+2+3+4+|2+3+4+5+|3+4+5+6+", joined_held_dice):
            return SMALL_STRAIGHT_SCORE()
        else:
            return DEFAULT_SCORE()


def calculate_full_house_score(score_choice: str, held_dice: list) -> int:
    """
    Calculate the full house score.

    A function that calculates the score of a category that requires a pair with a 3 of a kind and returns the result.

    :param score_choice: a string of the category name
    :param held_dice: a list of the held dice
    :precondition: score_choice must be a string of a numbered category found on the scorecard
    :precondition: held_dice must be a list
    :postcondition: returns the correct score
    :return: calculated full house score

    >>> doc_score_choice = "9 - Full House"
    >>> doc_held_dice = [1, 2, 3, 4, 6]
    >>> calculate_full_house_score(doc_score_choice, doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    0
    """
    held_dice_as_strings = [str(dice) for dice in held_dice]
    joined_held_dice = "".join(held_dice_as_strings)

    if score_choice == "9 - Full House":
        if re.match(r"^([1-6])\1{2}([1-6])\2$", joined_held_dice):
            return FULL_HOUSE_SCORE()
        elif re.match(r"^([1-6])\1([1-6])\2{2}$", joined_held_dice):
            return FULL_HOUSE_SCORE()
        else:
            return DEFAULT_SCORE()


def calculate_total_of_all_dice_score(score_choice: str, held_dice: list) -> int:
    """
    Calculate the "total of all dice" score.

    A function that calculates the score of a category that takes the sum of all face values of each dice and returns
    the result.

    :param score_choice: a string of the category name
    :param held_dice: a list of the held dice
    :precondition: score_choice must be a string of a numbered category found on the scorecard
    :precondition: held_dice must be a list
    :postcondition: returns the correct score
    :return: calculated "total of all dice" score

    >>> doc_choice = "7 - 3 of a kind"
    >>> doc_held_dice = [1, 1, 1, 1, 5]
    >>> calculate_total_of_all_dice_score(doc_choice, doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    9
    """
    held_dice_as_strings = [str(dice) for dice in held_dice]
    joined_held_dice = "".join(held_dice_as_strings)

    total_of_all_dice = DEFAULT_SCORE()
    for dice in held_dice:
        total_of_all_dice += dice

    if score_choice == "7 - 3 of a kind":
        if re.match(r".*([1-6])\1{2}.*", joined_held_dice):
            return total_of_all_dice
        else:
            return DEFAULT_SCORE()

    elif score_choice == "8 - 4 of a kind":
        if re.match(r".*([1-6])\1{3}.*", joined_held_dice):
            return total_of_all_dice
        else:
            return DEFAULT_SCORE()

    elif score_choice == "13 - Chance":
        return total_of_all_dice


def calculate_upper_score(score_choice: str, held_dice: list) -> int:
    """
    Calculate the upper score.

    A function that calculates the score of a category found in the upper section of the scorecard and returns the
    result.

    :param score_choice: a string of the category name
    :param held_dice: a list of the held dice
    :precondition: score_choice must be a string of a numbered category found on the scorecard
    :precondition: held_dice must be a list
    :postcondition: returns the correct score
    :return: calculated upper score

    >>> doc_choice = "5 - Fives"
    >>> doc_held_dice = [1, 1, 1, 1, 5]
    >>> calculate_upper_score(doc_choice, doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    5
    """
    if score_choice == "1 - Aces":
        category_score = held_dice.count(1) * ACES_SCORE()
        return category_score

    elif score_choice == "2 - Twos":
        category_score = held_dice.count(2) * TWOS_SCORE()
        return category_score

    elif score_choice == "3 - Threes":
        category_score = held_dice.count(3) * THREES_SCORE()
        return category_score

    elif score_choice == "4 - Fours":
        category_score = held_dice.count(4) * FOURS_SCORE()
        return category_score

    elif score_choice == "5 - Fives":
        category_score = held_dice.count(5) * FIVES_SCORE()
        return category_score

    elif score_choice == "6 - Sixes":
        category_score = held_dice.count(6) * SIXES_SCORE()
        return category_score


def calculate_score(scorecard: dict, current_player: str, score_choice: str, held_dice: list) -> int:
    """
    Calculate the score.

    A function that calculates the amount of points a roll is worth depending on the player's category choice and
    returns the results.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :param score_choice: a string of the category name
    :param held_dice: a list of the held dice
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :precondition: score_choice must be a string of a numbered category found on the scorecard
    :precondition: held_dice must be a list
    :postcondition: returns the correct score
    :return: calculated category score

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> doc_choice = "5 - Fives"
    >>> doc_held_dice = [1, 1, 1, 1, 5]
    >>> calculate_score(doc_scorecard, doc_player, doc_choice, doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    5
    """
    if re.match(r"^[1-6] - ", score_choice):
        category_score = calculate_upper_score(score_choice, held_dice)
        return category_score

    elif re.match(r"^7|8|13 - ", score_choice):
        category_score = calculate_total_of_all_dice_score(score_choice, held_dice)
        return category_score

    elif re.match(r"^9 - ", score_choice):
        category_score = calculate_full_house_score(score_choice, held_dice)
        return category_score

    elif re.match(r"^10 - ", score_choice):
        category_score = calculate_small_straight_score(score_choice, held_dice)
        return category_score

    elif re.match(r"^11 - ", score_choice):
        category_score = calculate_large_straight_score(score_choice, held_dice)
        return category_score

    elif re.match(r"^12 - ", score_choice):
        category_score = calculate_yahtzee_score(scorecard, current_player, held_dice)
        return category_score


def choose_score(scorecard: dict, current_player: str, held_dice: list) -> str:
    """
    Select the desired category.

    A function that asks the player to choose the category they want to use their dice on and returns their selection.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :param held_dice: a list of the held dice
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :precondition: held_dice must be a list
    :postcondition: returns the correct selection
    :return: player's selection
    """
    invalid_choice = True
    choices = {"1": "1 - Aces", "2": "2 - Twos", "3": "3 - Threes", "4": "4 - Fours", "5": "5 - Fives",
               "6": "6 - Sixes", "7": "7 - 3 of a kind", "8": "8 - 4 of a kind", "9": "9 - Full House",
               "10": "10 - Small Straight", "11": "11 - Large Straight", "12": "12 - Yahtzee", "13": "13 - Chance"}

    while invalid_choice:
        try:
            score_choice_number = input(f"\nPlease enter the number of the score you would like to update: ")
            score_choice = choices[score_choice_number]
            selection = scorecard[current_player][score_choice]

            if int(score_choice_number) not in range(1, 14):
                raise ValueError
            elif (selection != NO_SCORE() and selection != YAHTZEE_SCORE()) or is_yahtzee(held_dice) is False and \
                    selection == YAHTZEE_SCORE():
                raise ValueError
            else:
                return score_choice

        except (ValueError, KeyError):
            print(f"That is not a valid input! Please try again.")


def display_held_dice(held_dice: list):
    """
    Display the held dice.

    A function that prints the list of dice that are being held.

    :param held_dice: a list of the held dice
    :precondition: held_dice must be a list
    :postcondition: prints the correct list of held dice

    >>> doc_held_dice = [1, 1, 1, 1, 5]
    >>> display_held_dice(doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    You are holding the following dice: [1, 1, 1, 1, 5].
    ⚀ ⚀ ⚀ ⚀ ⚄
    """
    print(f"\nYou are holding the following dice: {held_dice}.")
    display_dice_images(held_dice)


def rolled_yahtzee():
    """
    Get excited!

    A function that shouts YAHTZEE at the top of its lungs by printing it in all caps and with many exclamation marks.

    :postcondition: prints Yahtzee in all caps and with many exclamation marks

    >>> rolled_yahtzee() # doctest: +NORMALIZE_WHITESPACE
    YAHTZEE!!!
    """
    print(f"YAHTZEE!!!")


def is_yahtzee(held_dice) -> bool:
    """
    Check if the held dice contains a Yahtzee.

    A function that checks if the held dice contains a 5 of a kind and returns a Boolean value depending on the result.

    :param held_dice: a list of the held dice
    :precondition: held_dice must be a list
    :postcondition: returns the correct answer to the question "is this a Yahtzee?"
    :return: Boolean value

    >>> doc_held_dice = [1, 1, 1, 1, 1]
    >>> is_yahtzee(doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    True
    """
    held_dice_as_strings = [str(dice) for dice in held_dice]
    joined_held_dice = "".join(held_dice_as_strings)

    if re.match(r"^([1-6])\1{4}$", joined_held_dice):
        return True
    else:
        return False


def choose_dice(held_dice: list) -> list:
    """
    Remove the selected dice.

    A function that asks the player to select the dice that they would like to re-roll, removes them from the list of
    held dice, and returns the list of the remaining dice.

    :param held_dice: a list of the held dice
    :precondition: held_dice must be a list
    :postcondition: returns the correct list of held dice
    :return: held dice
    """
    not_finished = True
    while not_finished:
        display_held_dice(held_dice)

        held_dice_as_strings = [str(dice) for dice in held_dice]
        joined_held_dice = "".join(held_dice_as_strings)

        roll_again = input(f"Please enter a number you would like to re-roll or 0 to keep all of your dice: ")
        if roll_again == "0":
            not_finished = False
        elif re.match(r"^[1-6]$", roll_again) and roll_again in joined_held_dice:
            held_dice.remove(int(roll_again))
        else:
            print_dice_choice_error()
    return held_dice


def print_dice_choice_error():
    """
    Print a helpful error message.

    A function that prints an error message after the player chooses to re-roll a dice that they do not have.

    :postcondition: prints the correct error message

    >>> print_dice_choice_error() # doctest: +NORMALIZE_WHITESPACE
    None of your dice have that value! Please try again.
    """
    print(f"None of your dice have that value! Please try again.")


def display_dice_images(held_dice: list):
    """
    Display the list of dice as images.

    A function that prints a list of dice as images with the correct faces.

    :param held_dice: a list of the rolled dice being held
    :precondition: held_dice must be a list
    :postcondition: prints the correct list of dice as images

    >>> doc_held_dice = [1, 2, 3, 4, 5]
    >>> display_dice_images(doc_held_dice)
    ⚀ ⚁ ⚂ ⚃ ⚄
    """
    held_dice_as_strings = [str(dice) for dice in held_dice]
    joined_held_dice = " ".join(held_dice_as_strings)

    dice_images = joined_held_dice.replace("1", "\u2680")
    dice_images = dice_images.replace("2", "\u2681")
    dice_images = dice_images.replace("3", "\u2682")
    dice_images = dice_images.replace("4", "\u2683")
    dice_images = dice_images.replace("5", "\u2684")
    dice_images = dice_images.replace("6", "\u2685")
    print(dice_images)


def display_rolled_dice(held_dice: list):
    """
    Display the rolled dice.

    A function that displays the list of dice that were rolled.

    :param held_dice: a list of the rolled dice being held
    :precondition: held_dice must be a list
    :postcondition: prints the correct list of rolled dice

    >>> doc_held_dice = [1, 1, 1, 1, 5]
    >>> display_rolled_dice(doc_held_dice) # doctest: +NORMALIZE_WHITESPACE
    You rolled the following dice: [1, 1, 1, 1, 5].
    ⚀ ⚀ ⚀ ⚀ ⚄
    """
    print(f"\nYou rolled the following dice: {held_dice}.")
    display_dice_images(held_dice)


def roll_dice(held_dice: list) -> list:
    """
    Roll some dice.

    A function that rolls some dice until there is 5 different rolls, gets excited if the roll is a Yahtzee, and
    returns a list of the sorted rolls.

    :param held_dice: a list of the held dice
    :precondition: held_dice must be a list
    :postcondition: returns the correct list of held dice
    :return: held dice
    """
    total_number_of_dice = 5
    number_of_dice_to_roll = total_number_of_dice - len(held_dice)

    for _ in range(number_of_dice_to_roll):
        roll = random.randint(1, 6)
        held_dice.append(roll)
    held_dice = sorted(held_dice)

    is_roll_yahtzee = is_yahtzee(held_dice)
    if is_roll_yahtzee:
        rolled_yahtzee()

    return held_dice


def rolls() -> list:
    """
    Determine the dice rolls.

    A function that allows a player to roll 5 separate dice up to 3 times each and returns a list of the face values
    after the final roll.

    :postcondition: returns the correct list of held dice
    :return: held dice
    """
    dice_roll_counter = 0
    number_of_rolls_that_can_roll_again = 2
    maximum_number_of_rolls = 3
    total_number_of_dice = 5

    held_dice = []
    while dice_roll_counter < maximum_number_of_rolls:
        input(f"\nPress enter to roll the dice.")
        held_dice = roll_dice(held_dice)
        display_rolled_dice(held_dice)

        if dice_roll_counter < number_of_rolls_that_can_roll_again:
            held_dice = choose_dice(held_dice)
        if len(held_dice) == total_number_of_dice:
            dice_roll_counter += 2

        dice_roll_counter += 1

    return held_dice


def display_scorecard(scorecard: dict, current_player: str):
    """
    Display the score.

    A function that prints the scorecard of the current player.

    :param scorecard: a non-empty dictionary of the scorecards
    :param current_player: a string of the current player
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: current_player must be "Player 1" or "Player 2"
    :postcondition: prints the correct player's scorecard

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player = "Player 1"
    >>> display_scorecard(doc_scorecard, doc_player) # doctest: +NORMALIZE_WHITESPACE
    1 - Aces : -1
    2 - Twos : -1
    3 - Threes : -1
    4 - Fours : -1
    5 - Fives : -1
    6 - Sixes : -1
    Upper Subtotal : -1
    Bonus : -1
    Upper Total : -1
    7 - 3 of a kind : -1
    8 - 4 of a kind : -1
    9 - Full House : -1
    10 - Small Straight : -1
    11 - Large Straight : -1
    12 - Yahtzee : -1
    13 - Chance : -1
    Yahtzee Bonus : 0
    Lower Total : -1
    Grand Total : -1
    """
    print()

    for key, value in scorecard[current_player].items():
        print(f"{key} : {value}")


def check_if_out_of_turns(scorecard: dict, player_number: str) -> bool:
    """
    Check if the player has any turns left.

    A function that checks if the current player's scorecard has any categories with -1 left and returns a Boolean
    value depending on the result.

    :param scorecard: a non-empty dictionary of the scorecards
    :param player_number: a string of the input player number
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :precondition: player_number must be either "1" or "2"
    :postcondition: returns the correct answer to the question "is this player out of turns?"
    :return: Boolean value

    >>> doc_scorecard = {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}, 'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, \
    '5 - Fives': -1, '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, \
    '7 - 3 of a kind': -1, '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, \
    '11 - Large Straight': -1, '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, \
    'Grand Total': -1}}
    >>> doc_player_number = "1"
    >>> check_if_out_of_turns(doc_scorecard, doc_player_number) # doctest: +NORMALIZE_WHITESPACE
    False
    """
    player = f"Player {player_number}"

    for value in scorecard[player].values():
        if value == NO_SCORE():
            return False

    return True


def whose_turn(scorecard: dict) -> str:
    """
    Ask the user's player number.

    A function that asks the player which player number they are and returns the result if they have at least one turn
    remaining.

    :param scorecard: a non-empty dictionary of the scorecards
    :precondition: scorecard must be a non-empty dictionary of the scorecard template
    :postcondition: returns the correct string representing the current player number
    :return: current player number
    """
    invalid_player_number = True

    while invalid_player_number:
        try:
            player_number = input(f"\nPlease enter your player number (1 or 2): ")

            if int(player_number) not in range(1, 3):
                raise ValueError
            elif check_if_out_of_turns(scorecard, player_number):
                raise ValueError

            current_player = f"Player {player_number}"
            return current_player

        except ValueError:
            print(f"That is not a valid input or you are out of turns! Please try again.")


def load_scorecard() -> dict:
    """
    Load the scorecard.

    A function that loads a scorecard template in a JSON file and returns the result dictionary.

    :precondition: filename must be the string name of a file in the same directory
    :postcondition: returns the correct dictionary containing the scorecards
    :return: dictionary of scorecards

    >>> load_scorecard() # doctest: +NORMALIZE_WHITESPACE
    {'Player 1': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1, \
    '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, '7 - 3 of a kind': -1, \
    '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, '11 - Large Straight': -1, \
    '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}, \
    'Player 2': {'1 - Aces': -1, '2 - Twos': -1, '3 - Threes': -1, '4 - Fours': -1, '5 - Fives': -1, \
    '6 - Sixes': -1, 'Upper Subtotal': -1, 'Bonus': -1, 'Upper Total': -1, '7 - 3 of a kind': -1, \
    '8 - 4 of a kind': -1, '9 - Full House': -1, '10 - Small Straight': -1, '11 - Large Straight': -1, \
    '12 - Yahtzee': -1, '13 - Chance': -1, 'Yahtzee Bonus': 0, 'Lower Total': -1, 'Grand Total': -1}}
    """
    filename = "scorecard.JSON"
    try:
        with open(filename) as file_object:
            scorecard = json.load(file_object)
            return scorecard
    except FileNotFoundError:
        print(f"The file was not found.")


def display_game_intro():
    """
    Display the introduction to the game.

    A function that prints the name of the game and a short introduction oh how to play.

    :postcondition: prints the correct introduction to the game.

    >>> display_game_intro() # doctest: +NORMALIZE_WHITESPACE
    Welcome to:
                            #     #    #    #     # ####### ####### ####### #######
                            #     #    #    #     # ####### ####### ####### #######
                              # #    #   #  #     #    #        #   #       #
                               #    #     # #######    #       #    #####   #####
                               #    ####### #     #    #      #     #       #
                               #    #     # #     #    #     #      #       #
                               #    #     # #     #    #    ####### ####### #######
    Yahtzee is a game that involves rolling 5 dice and trying to outscore your opponent.
    Earn as many points as possible by going for specific combinations and bonus points.
    Be strategic and may the dice roll in your favour!
    """
    print(f"\nWelcome to:\n")
    print(f"                        #     #    #    #     # ####### ####### ####### #######")
    print(f"                        #     #    #    #     # ####### ####### ####### #######")
    print(f"                          # #    #   #  #     #    #        #   #       #      ")
    print(f"                           #    #     # #######    #       #    #####   #####  ")
    print(f"                           #    ####### #     #    #      #     #       #      ")
    print(f"                           #    #     # #     #    #     #      #       #      ")
    print(f"                           #    #     # #     #    #    ####### ####### #######\n")
    print(f"Yahtzee is a game that involves rolling 5 dice and trying to outscore your opponent.\n"
          f"Earn as many points as possible by going for specific combinations and bonus points.\n"
          f"Be strategic and may the dice roll in your favour!")


def yahtzee():
    """
    Play a game of Yahtzee.

    A function that allows two players to play a friendly game of Yahtzee and announces the player with the higher
    score as the winner.

    :postcondition: prints the correct winner of the game
    """
    display_game_intro()

    game_not_over = True
    scorecard = load_scorecard()

    while game_not_over:
        player = whose_turn(scorecard)
        display_scorecard(scorecard, player)

        held_dice = rolls()

        display_scorecard(scorecard, player)
        choice = choose_score(scorecard, player, held_dice)

        score = calculate_score(scorecard, player, choice, held_dice)
        update_scorecard(scorecard, player, choice, score)

        game_not_over = is_the_game_not_over(scorecard)

    outcome = determine_outcome(scorecard)
    display_scorecard(scorecard, "Player 1")
    display_scorecard(scorecard, "Player 2")
    display_outcome(scorecard, outcome)


def main():
    """
    Drive the program.
    """
    yahtzee()
    # doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
