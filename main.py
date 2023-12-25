from word_dictionary import *
from check_string_functions import *
from hangman_strings import *
from helpers import *
from time import sleep

# import dictionary
word_dict = word_dictionary_create('WordDictionary_Hangman.csv')

# create empty dictionary to keep track of words that have been used by the game during session and
# whether those were successes or failures
win_loss_dict = {}
key_list = []

# Open user settings assign contents to an array and create an empty dictionary for storing
settings_file = open('settings.txt', 'r')
settings_array = settings_file.readlines()
dict_settings = {}

# Load settings into dictionary for reference
for line in settings_array:
    line.replace('\n', '')
    if line.find('=') > 0:
        dict_settings[line[:line.find('=')].strip()] = line[line.find('=') + 1:].strip()

settings_file.close()


def update_settings(f_value, text_speed):
    """(int, str)

    update values in dict_settings

    """
    if dict_settings['text_speed'] != text_speed:
        dict_settings['text_speed'] = text_speed
    if dict_settings['filter_value'] != f_value:
        dict_settings['filter_value'] = f_value


def apply_text_speed(text_speed_setting):

    text_mode_fast = 'fast'
    text_mode_slow = 'slow'

    no_pause = 0

    if text_speed_setting == text_mode_fast:
        big_pause = no_pause
        small_pause = no_pause
    else:
        big_pause = 1
        small_pause = 0.5

    return [big_pause, small_pause]


    # begin main game loop. While the word is not fully guessed, and the total
    # incorrect guesses is less than 6, continue allowing guesses
    # after each guess, check if the letter is correct and if so, return the number of correct
    # characters and their indexes, this info will be used to populate the graphic feedback
def main():
    finished_words_str = ''
    filter_word_amount = int(dict_settings['filter_value'])  # get filter settings from dict
    text_mode = dict_settings['text_speed']  # get text speed settings from dict
    text_settings = apply_text_speed(text_mode)
    big_pause = text_settings[0]
    small_pause = text_settings[1]


    # /////// Round Loop //////// #
    while True:
        word_to_guess = get_word(word_dict, filter_word_amount, win_loss_dict) # get word_to_guess from dict
        key_list.append(word_to_guess) # append generated word to the word list for later reference
        correct_counter = 0 # initialize correct counter
        incorrect_counter = 0 # initialize incorrect counter
        guesses_string = '' # intialize string to track letter guesses
        quit_string = 'quit'
        is_big_word = len(word_to_guess) > 6 # check if incorrect_counter needs to be increased
        word_progress_string = '_ ' * len(word_to_guess) #generate a blank progress string

        # change max guesses based on the length of the word_to_guess
        if is_big_word:
            incorrect_counter_max = big_word
        else:
            incorrect_counter_max = small_word

        # Provide alternative input options to user
        print("\nIf you wish to change text speed or word filter settings at any point during the game please type 'settings'")
        print(f'\nIf you wish to quit at any point, type "{quit_string}"\n')
        sleep(2)

        # ////// Guess Loop ////// #

        while True:
            # print current game information
            print(f'The word is {len(word_to_guess)} letters long')
            print(f'You have {incorrect_counter_max} guesses to get the word\n')
            sleep(big_pause)
            print(f'{load_hangman(incorrect_counter, incorrect_counter_max)}         Answer:   {word_progress_string}')
            print(f'\nCharacters already guessed: {guesses_string}\n')
            sleep(small_pause)

            # Input for user guess
            guess_prompt = pre_process_input(f'Guess a letter or word: ', text_mode, filter_word_amount)

            # Update letter_guess and settings information
            letter_guess = guess_prompt.input_str
            filter_word_amount = guess_prompt.f_value
            text_mode = guess_prompt.speed
            update_settings(guess_prompt.f_value, guess_prompt.speed)
            text_settings = apply_text_speed(guess_prompt.speed)
            big_pause = text_settings[0]
            small_pause = text_settings[1]
            guess_length = len(letter_guess)

            # check if the input is valid, and if so, if it is contained in the word_to_gues
            error_code = has_invalid_character(letter_guess, guesses_string)
            if error_code != no_error:
                sleep(small_pause)
                print(error_codes[error_code] + '\n')
                sleep(big_pause)
                continue

            # quit check
            if letter_guess.lower() == quit_string:
                break

            # get object for guess_info
            guess_info = resolve_guess(word_to_guess, letter_guess)

            # In the case of a word guess, check if they got it right. The correct_guesses
            # value should equal the length of the word_to_guess in this case
            if guess_info.correct_count == len(word_to_guess):
                correct_counter = len(word_to_guess)

            # if the user guessed a word or letter incorrect increment the incorrect counter
            elif guess_info.correct_count == 0:
                sleep(small_pause)
                incorrect_counter += 1
                if not guess_length > 1:
                    print(f"'{letter_guess}' is not in the word")
                else:
                    print(f"'{letter_guess}' is not the word")
                sleep(big_pause)

            # if the user got a letter guess right, increment the correct letters
            elif guess_info.correct_count > 0:
                sleep(small_pause)
                print(f"found '{letter_guess}' in word")
                sleep(big_pause)
                correct_counter += guess_info.correct_count

            # update the place holder string with the appropriate letters
            word_progress_string = generate_word_progress(word_progress_string, guess_info.indices, guess_info.letters)

            # append a comma if the user has guessed at least one valid character
            if len(guesses_string) > 0 and len(letter_guess) == 1:
                guesses_string += ', '

            if not guess_length > 1:
                # append guess to guess string
                guesses_string += letter_guess

            if check_win_loss(incorrect_counter, correct_counter, incorrect_counter_max, len(word_to_guess)):
                break

            # new line
            print()

        # new line
        print(f'\n{load_hangman(incorrect_counter, incorrect_counter_max)}         Answer:   {word_progress_string}')

        #new line
        print()

        # add the word_to_guess to the dictionary with an empty value
        win_loss_dict[str(word_to_guess)] = ''

        # after playing, if the player completed the game in less than 6 guess they won!
        if correct_counter == len(word_to_guess):
            print(f'Congrats! You guessed correctly, the word was "{word_to_guess}". '
                  f'You got it right with {incorrect_counter_max - incorrect_counter} guesses left\n')

            # set value of new dict entry to 'Win'
            win_loss_dict[str(word_to_guess)] = 'Win'

        else:
            print(f"Oh no! You weren't able to guess the word, "
                  f"the correct answer was '{word_to_guess}'. You got {correct_counter} "
                  f"correct letters\n")

            # set value of new dict entry to 'Loss'
            win_loss_dict[str(word_to_guess)] = 'Loss'

        # add the current word to the finished words string to track that it has been attempted
        finished_words_str += str(key_list[len(key_list)-1])
        print(f"Words you've attempted so far: {finished_words_str}\n")
        sleep(big_pause)

        # check if user wishes to continue
        continue_prompt = f'Would you like to play again? {yes_str} / {no_str}: '

        # check tha the user responds with a valid y / n response
        while True:
            continue_response = pre_process_input(continue_prompt, text_mode, filter_word_amount)
            update_settings(continue_response.f_value, continue_response.speed)
            text_settings = apply_text_speed(continue_response.speed)
            text_mode = continue_response.speed
            filter_word_amount = continue_response.f_value
            big_pause = text_settings[0]
            small_pause = text_settings[1]
            print()
            sleep(small_pause)

            # on invalid input reprompt to user
            if continue_response.input_str not in [yes_str, no_str]:
                continue_prompt = f'Invalid input, please enter {yes_str} or {no_str}: '
                continue
            else:
                break # break the guess loop

        # if the user responds 'n' break out of the round loop
        if not check_continue(continue_response.input_str):
            break

        # append comma to finished_words_str only if the user chooses to continue playing
        finished_words_str += ', '

    print('\nThanks for playing! :)')

    settings_file = open('settings.txt', 'w')

    # write settings dictionary entries to the settings file before ending the program.
    for line in dict_settings:
        settings_file.write(f'{line} = {dict_settings[str(line)]}\n')

    settings_file.close()

# run main
if __name__ == '__main__':
    main()
