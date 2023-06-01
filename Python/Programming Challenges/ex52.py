# Mr Stratton
# 01/06/2023
# Programming Challenges 52
# SQA Computing Science National 5

import random

number = random.randint(97, 122)

print('Guess which letter of the alphabet is')
print('represented in ASCII by the letter -', number)
guess = input('>')

while ord(guess) != number:
    print('Sorry', guess, 'would be', ord(guess))
    guess = input('>')

print('Correct,', guess, '=', number)