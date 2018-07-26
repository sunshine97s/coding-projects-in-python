def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 1:
        if guess.lower() == answer.lower():
            print("You're right!")
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Wrong! Try again: ')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct answer was ' + answer)
score = 0
print('Guess the Animal!')
guess1 = input('Which bear lives at the North Pole: ')
check_guess(guess1, 'polar bear')
guess2 = input('Which is the fastest land animal: ')
check_guess(guess2, 'cheetah')
guess3 = input('Which is the largest animal: ')
check_guess(guess3, 'blue whale')
guess4 = input('Which animal has a long trunk: ')
check_guess(guess4, 'elephant')
guess5 = input('Which mammal can fly: ')
check_guess(guess5, 'bat')
guess6 = input('How many hearts does an octopus have: ')
check_guess(guess6, '3')
guess7 = input('Which one of these is a fish?\n A) Whale\n B) Dolphin\n C) Shark\n D) Squid Type A, B, C or D: ')
check_guess(guess7, 'c')
guess8 = input('Rhinos are herbivores. True or False: ')
check_guess(guess8, 'True')
print('Your score is ' + str(score))