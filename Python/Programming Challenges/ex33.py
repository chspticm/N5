# Mr Stratton
# 30/05/2023
# Programming Challenges 33
# SQA Computing Science National 4

print('Would you like some advice?')
answer = input('>')

while answer != 'Y':
    if answer == 'N':
        print('Don\'t be silly. You definitely need advice!')
    else:
        print('You must enter Y or N')
    print('Would you like some advice?')
    answer = input('>')

print('Don\'t feed the Trolls!')