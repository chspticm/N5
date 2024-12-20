# Mr Stratton
# 31/05/2023
# Programming Challenges 32
# SQA Computing Science National 4

password = '1234'

print('Please enter the password.')
userEntry = input('>')

while userEntry != password:
    print('Sorry, Incorrect! Try Again')
    print('Please enter the password.')
    userEntry = input('>')

print('Entry gained!')
