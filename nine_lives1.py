import random

lives = 9
words = ['pizza', 'shirt', 'otter', 'plane', 'lives', 'light']
secret_word = random.choice(words)
clue = list('?????')
unknown_letters = len(secret_word)
heart_symbol, wolf = u'\u2764', u'\U0001F43A'
guess_word_correctly = False

difficulty = input('Choose a level: Type 1, 2 or 3:\n 1: Easy\n 2: Medium\n 3: Hard Which will you choose: ')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
elif difficulty == 3:
    lives = 6

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives left: ' + wolf * lives)
    guess = input('Guess a letter or the full word: ')

    if guess == secret_word:
        guess_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Sorry! You lost a life!')
        lives = lives - 1

if guess_word_correctly:
    print('Congratulations! You won! The secret word you were guessing was: ' + secret_word)
else:
    print('Too bad! You lost, but keep trying! The secret word was: ' + secret_word)
