import random
import string

adjectives = ['sleepy', 'slow','swift','cold','large','elemental','wise','fierce','brave']
elements = ['fire','water','earth','air','electric','light','darkness','spiritual','spiral']
nouns = ['elk','pteradactyl','owl','deer','wolf','dragon','snake','phoenix','icetalon']
print('Welcome to Password Picker!')

while True:
    for x in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        element = random.choice(elements)
        number = random.randrange(0,100)
        special_char = random.choice(string.punctuation)
        password = adjective + element + noun + str(number) + special_char
        print('Your new password is: %s' % password)
    response = input('Do you like your new password? Type yes or no: ')
    if response == 'no':
        break
