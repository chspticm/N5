# Mr Stratton
# 01/06/2023
# Programming Challenges 47
# SQA Computing Science National 5

import random
score = 0

for loop in range(10):
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)

    print('I have generated two random numbers')
    print('Which is the largest, 1 or 2?')
    print('Enter your choice.')
    choice = int(input('>'))

    print('Number 1 =',number1)
    print('Number 2 =',number2)

    if choice == 1 and number1 > number2:
        print('Correct, number 1 was the largest')
        score = score + 1
    elif choice == 2 and number2 > number1:
        print('Correct, number 2 was the largest')
        score = score + 1
    else:
        print('sorry you were wrong')

print('Your final score was', score, 'correct.')
