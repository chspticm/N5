# Mr Stratton
# 31/05/2023
# Programming Challenges 46
# SQA Computing Science National 5

import random

randomNumber = random.randint(1, 100)

print('Guess the hidden number between 1 and 100')
print('Enter your guess')
guess = int(input('>'))

while guess != randomNumber:
    if guess > randomNumber:
        print('Your guess is too high. Try again')
    elif guess < randomNumber:
        print('Your guess is too low. Try again')

    guess = int(input('>'))

print('Correct! Well Done')
    