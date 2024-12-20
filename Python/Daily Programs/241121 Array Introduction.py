# Introduction to Arrays
# Mr Stratton
# 21/11/24

name = ['' for x in range(5)]
age = [0 for x in range(5)]

for index in range(5):
    name[index] = input('Name? >')

for x in range(5):
    print(name[x])
