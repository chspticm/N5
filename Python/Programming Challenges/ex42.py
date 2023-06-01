# Mr Stratton
# 01/06/2023
# Programming Challenges 42
# SQA Computing Science National 5

name = ['' for x in range(4)]
age = [0 for x in range(4)]

for index in range(4):
    print('Please enter a name:')
    name[index] = input('>')
    print('Please enter',name[index] + '\'s age:')
    age[index] = int(input('>'))

print('Names and Competition List:')
for x in range(4):
    if age[x] < 12:
        level = 'Junior'
    elif age[x] >= 18:
        level = 'Senior'
    else:
        level = 'Teen'

    print(name[x], '-', level)