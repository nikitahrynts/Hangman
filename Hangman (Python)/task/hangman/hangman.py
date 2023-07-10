import random
import string

WIN_COUNT = 0
LOSE_COUNT = 0

list_of_words = ['python', 'java', 'swift', 'javascript']


def play_game():

    total_attempts = 8
    word_to_guess = random.choice(list_of_words)
    letters_in_word = set(word_to_guess)
    letters = list('-' * len(word_to_guess))
    used_letters = set()
    has_won = False

    while total_attempts > 0:

        print(''.join(letters))
        guess = input('Input a letter: ')
        if len(guess) > 1 or guess == '':
            print('Please, input a single letter.\n')
            continue
        elif guess.isupper() or guess not in string.ascii_letters:
            print('Please, enter a lowercase letter from the English alphabet.\n')
            continue

        position = -1
        if guess in letters_in_word:
            for letter in word_to_guess:
                position += 1
                if guess == letter:
                    letters[position] = letter
            letters_in_word.discard(guess)
            used_letters.add(guess)
            print()
        elif guess in used_letters and len(letters_in_word) > 0:
            print("You've already guessed this letter.\n")
        else:
            print("That letter doesn't appear in the word.\n")
            used_letters.add(guess)
            total_attempts -= 1

        if len(letters_in_word) == 0 and total_attempts >= 0:
            print(f'You guessed the word {word_to_guess}!',
                  'You survived!\n', sep='\n')
            has_won = True
            break
        elif len(letters_in_word) > 0 and total_attempts == 0:
            print('You lost!\n')

    if has_won:
        return True
    else:
        return False


print(f'H A N G M A N\n')
while True:
    menu_option = input('Type "play" to play the game,'
                        ' "results" to show the scoreboard,'
                        ' and "exit" to quit: ')
    if menu_option == 'play':
        if play_game():
            WIN_COUNT += 1
        else:
            LOSE_COUNT += 1
        continue
    elif menu_option == 'results':
        print(f'You won: {WIN_COUNT} times',
              f'You lost: {LOSE_COUNT} times\n',
              sep='\n')
        continue
    elif menu_option == 'exit':
        break
