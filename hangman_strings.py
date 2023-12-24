error_codes = [
 '',
 'Your guess must contain at least one character. Please try again',
 'Your guess contains a number, please ensure that your guess only contains one non-numeric characters',
 'Your guess contains non-alphabetic characters. Please only use characters contained in the alphabet',
 "You've already guessed that letter, please try a letter you haven't guessed yet"

]

hangman_str_six = [
    (f"    _______\n"
     f"|      |\n"
     f"|       \n"
     f"|       \n"
     f"|       \n"
     f"|       \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|        \n"
     f"|        \n"
     f"|         \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|       |\n"
     f"|       |\n"
     f"|        \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|       |\\\n"
     f"|       |\n"
     f"|        \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|      /|\\\n"
     f"|       |\n"
     f"|        \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|      /|\\\n"
     f"|       |\n"
     f"|      /   \n"
     f"|___"),

    (f"    _______\n"
     f"|       |\n"
     f"|      (_)\n"
     f"|      /|\\\n"
     f"|       |\n"
     f"|      / \\\n"
     f"|___")
]
hangman_str_eight = [
    (f"    _______\n"
     f"|      |\n"
     f"|       \n"
     f"|       \n"
     f"|       \n"
     f"|       \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|        \n"
     f"|        \n"
     f"|         \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|       |\n"
     f"|       |\n"
     f"|        \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|       |\\\n"
     f"|       |\n"
     f"|        \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|      /|\\\n"
     f"|       |\n"
     f"|        \n"
     f"|___"),

    (f"    _______\n"
     f"|/      |\n"
     f"|      (_)\n"
     f"|      /|\\\n"
     f"|       |\n"
     f"|      /   \n"
     f"|___"),

    (f"    _______\n"
     f"|       |\n"
     f"|      (_)\n"
     f"|      /|\\\n"
     f"|       |\n"
     f"|      / \\\n"
     f"|___"),

    (f"    _______\n"
     f"|       |\n"
     f"|     (^_)\n"
     f"|      /|\\\n"
     f"|       |\n"
     f"|      / \\\n"
     f"|___"),

    (f"    _______\n"
     f"|       |\n"
     f"|     (^_^)\n"
     f"|      /|\\\n"
     f"|       |\n"
     f"|      / \\\n"
     f"|___"),
]


def generate_word_progress(current_string, indices, guess):
    """(str, [], str] -> str

    For a given progress string, list of indices, and a letter guess, return a new progress string
    with the positions of the guess updated.

    >> generate_word_progress('a _ _ s _ m e', [4], 'o')
    'a _ _ s o m e'
    > generate_word_progress('a _ _ e a _', [1,2], 'p')
    a p p e a _
    """

    # transform place_holder_string in to a list, so that we can
    # replace individual letters within string
    place_holder_list = list(current_string)

    # for each entry in the list replace _ with the guessed letter
    # the rejoin the characters into a string
    j = 0
    for i in indices:
        place_holder_list[i * 2] = guess[j]
        j += 1

    # reassemble the list as a string
    place_holder_string = ''.join(place_holder_list)

    return place_holder_string
