# Mr Stratton
# 31/05/2023
# Programming Challenges 54
# SQA Computing Science National 5

import random

print('Your letters are:')
for loop in range(7):
    rndNo = random.randint(65, 90)
    letter = chr(rndNo)

    if letter in 'AEIOULNSTR':
        points = 1
    elif letter in 'DG':
        points = 2
    elif letter in 'BCMP':
        points = 3
    elif letter in 'FHVWY':
        points = 4
    elif letter == 'K':
        points = 5
    elif letter in 'JX':
        points = 8
    elif letter in 'QZ':
        points = 10
    else:
        print('An error has occured.')

    print(letter, '-', points)