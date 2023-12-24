import random

yes_str = 'y'
no_str = 'n'


class GuessInfo:
    def __init__(self, correct_guesses, placement_indices, correct_letters):
        self.correct_count = correct_guesses
        self.indices = placement_indices
        self.letters = correct_letters


def has_number(str1):
    """(str) -> bool

    Check if a given string contains numbers. If it does, return True, if not return False

    >>has_number('hello')
    false
    >>has_number('l0ve')
    true

    """
    for char in str1:
        if char.isnumeric():
            return True


def is_alpha(guess):
    """(str) -> bool

    For a given string, return True if the string contains only alphabetical characters.
    Return false if other characters are present.

    >> is_alpha('hi')
    True
    >> is_alpha(w8)
    False

    """

    for char in guess:
        if char.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True


def check_continue(cont_yes_no):
    if cont_yes_no == yes_str:
        return True
    elif cont_yes_no == no_str:
        return False


def resolve_guess(word, guess):
    """(str, str) -> object{int, ar, arr}

    for a given string and guess letter provide the number of times
    the letter appears in the string and their indexes

    The character must appear in the string for this function to work

    >>count_letter('lemon', 'm')
    [1, 2]
    >>count_letter('appreciate', 'p')
    [2, [1, 2]]

    """

    count = 0
    index = 0
    length = len(word)
    guess_size = len(guess)
    letters = []
    indices = []

    if guess_size > 1 and guess == word:
        indices = range(0, length, 1)
        letters = list(word)
        count = length

    elif guess_size > 1 and guess != word:
        count = 0

    else:
        for char in word:
            if guess == char:
                count += 1
                indices.append(index)
                letters.append(char)
            index += 1

    guess_info = GuessInfo(count, indices, letters)

    return guess_info
