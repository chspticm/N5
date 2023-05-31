# Mr Stratton
# 31/05/2023
# Programming Challenges 31
# SQA Computing Science National 5

print('The following program will display Odd Numbers')
print('Enter the first number in the list')
first = int(input('>'))
print('Enter the last number in the list')
last = int(input('>'))

print('Odd Number List')

for number in range(first, last + 1, 2):
    print(number)