# Mr Stratton
# 19/11/24
# Introduction to Arrays

name = ['' for x in range(5)]

for x in range(5):
    print('Please enter a name')
    name[x] = input('>')

print(name)

for x in range(5):
    print(name[x])