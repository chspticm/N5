# Mr Stratton
# 30/05/2023
# Programming Challenges 15

print('Please enter the first amount raised.')
first = int(input('>'))
print('Please enter the second amount raised.')
second = int(input('>'))
print('Please enter the third amount raised.')
third = int(input('>'))

total = first + second + third

print('A total of £' + str(total),'was raised.')

if total >= 1000:
    total = total * 2
    print('This will be doubled to £' + str(total))

