# Mr Stratton
# 31/05/2023
# Programming Challenges 35
# SQA Computing Science National 4

total = 0

print('Please enter the price of each present')
while total <= 200:
    money = int(input('>'))
    total = total + money

print('Limit Exceeded')
print('You can\'t include the £' + str(money), 'present') 