# Mr Stratton
# 31/05/2023
# Programming Challenges 38
# SQA Computing Science National 5

number = 56

print('Guess the hidden number between 1 and 100')
print('Enter your guess')
guess = int(input('>'))

while guess != number:
    if guess > number:
        print('Your guess is too high. Try again')
    elif guess < number:
        print('Your guess is too low. Try again')

    guess = int(input('>'))

print('Correct! Well Done')
    