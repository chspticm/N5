# Mr Stratton
# 19/11/24
# Introduction to Arrays

name = ['' for x in range(5)]
age = [0 for x in range(5)]
total = 0

for x in range(5):
    print('Please enter a name')
    name[x] = input('>')
    print('Please enter', name[x], 'age')
    age[x] = int(input('>'))

for x in range(5):
    total = total + age[x]
average = total / 5

for x in range(5):
    print(name[x],'-',age[x])

print('The average age is', average)