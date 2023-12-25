from hangman_strings import hangman_str_six, hangman_str_eight
from random import randint

small_word = 6
big_word = 8


# create output class
class PreProcessingOutput:
    def __init__(self, response_value, new_filter_value, new_text_speed_value):
        self.input_str = response_value
        self.f_value = new_filter_value
        self.speed = new_text_speed_value


def get_word(word_dict, filter_amount, win_loss_dict):
    """(dict) -> str

    return a word from the dictionary on call

    """
    # find length of dictionary for pick_index
    length_dict = len(word_dict)

    # generate a random number to get a word from the word_dict
    index = pick_index(length_dict)

    while True:
        # if the word length is longer than the filter value try again
        if int(word_dict[str(index)][2]) > filter_amount:
            index = pick_index(length_dict)

        # if the world has already be attempted try again
        elif word_dict[str(index)][0] in win_loss_dict.keys():
            index = pick_index(length_dict)
            print('Word repeated, generating new word')

        else:
            break

    return word_dict[str(index)][0]


def pick_index(length_dictionary):
    """(int) -> int

    Generate a random value between 1 and the length of the word_dict
    return the random value as int

    >>pick_index(635)

    """
    return randint(1, length_dictionary)


def load_hangman(guesses, max_guesses):
    """(int, int) -> str

    For a given guess value and a max guess value return
    a string corresponding to the current hangman situation

    >> load_hangman(2, 6)
            _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |___
    >> load_hangman(7,8)
        _______
    |       |
    |     (^_)
    |      /|\
    |       |
    |      / \
    |___
    """

    if max_guesses > small_word:
        return hangman_str_eight[guesses]
    else:
        return hangman_str_six[guesses]


def pre_process_input(prompt_string, text_speed, filter_value):
    """(str, str, int) -> class(str, int, str)

    For a given prompt, check if the user has requested the settings menu. If the user
    enters the settings menu, prompt the user for a text_speed and filter_value.
    Once the user has provided these options, re-prompt the user for the original
    prompt. Output the new information as a class.

    """

    # define key_word to access settings and store prompt response in a variable
    settings_key_word = 'settings'
    response = input(prompt_string)

    # check if the response contains keyword
    if response.lower() == settings_key_word:
        print('/////// SETTINGS ////////\n')

        print(f'Current settings: text_speed: {text_speed}, filter_value: {filter_value}\n')

        input_message = 'Would you like to change your filter setting? y/n: '

        while True:
            filter_change = input(input_message)
            if filter_change.lower() not in ['y', 'n']:
                input_message = 'Invalid input, please enter "y" or "n"'
                continue
            else:
                break

        if filter_change == 'y':

            # prompt for the filter settings
            input_message = 'Please enter a word length filter value of 5 or higher: '
            is_not_number = False

            # ensure that the response contains only numbers and does not fall below
            # the minimum filter value
            while True:
                filter_value = input(input_message)

                # check for non-numeric characters
                for char in filter_value:
                    if char not in '0123456789':
                        is_not_number = True

                # if there are non-numeric characters continue
                if is_not_number:
                    input_message = 'Invalid input, input should only contain numbers, please try again: '
                    continue

                # if the filter_value is below the minimum allowed value continue
                elif int(filter_value) < 5:
                    input_message = 'Please enter a value greater than 4 please enter a new value: '

                # break the loop if the input is valid continue to text_speed input
                else:
                    break

        input_message = 'Would you like to change your text_speed settings? y/n: '

        while True:
            text_speed_change = input(input_message)
            if text_speed_change.lower() not in ['y', 'n']:
                input_message = 'Invalid input, please enter either "y" or "n": '
                continue
            else:
                break

        if text_speed_change == 'y':

            # prompt for the text_speed setting
            input_message = 'Please enter your preferred text speed, either "fast" or "slow": '

            # ensure the response contains a valid keyword
            while True:
                text_speed = input(input_message)
                if text_speed.lower() not in ['fast', 'slow']:
                    input_message = 'Invalid input, please enter either "fast" or "slow": '
                else:
                    break

        # prompt the user again with the original prompt
        response = input(f'\n{prompt_string}')

    # create object containing all user inputs
    output_object = PreProcessingOutput(response.lower(), int(filter_value), text_speed)

    return output_object


def check_win_loss(incorrect, correct, max_incorrect, len_word_to_guess):
    """(int, int, int, int) -> bool

    For current incorrect and correct guesses, check if the play has lost or won. Return
    True is the user has won or lost, return false if the game should continue

    >> check_win_loss(3, 4, 6, 5)
    False
    >> check_win_loss(6, 3, 6, 5)
    True"""

    if incorrect == max_incorrect:
        return True

    elif correct == len_word_to_guess:
        return True

    else:
        return False
