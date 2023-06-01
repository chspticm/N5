# Mr Stratton
# 01/06/2023
# Programming Challenges 43
# SQA Computing Science National 5

import random
random.seed(10)

name   = ['Angus', 'Argo', 'Artax', 'Cisco', 'Flash', 'Lucky', 'Maximus', 'Mister Ed', 'Samson', 'Silver', 'Sonador', 'Spirit', 'Arod', 'Duchess', 'Black Beauty']
age    = [random.randint(5, 16) for x in range(15)]
height = [random.randint(12,18) for x in range(15)]

print('Please enter the details of your horse.')
print('Maximum height')
maxHeight = int(input('>'))
print('Maximum Age')
maxAge = int(input('>'))

for index in range(15):
    if height[index] <= maxHeight and age[index] <= maxAge:
        print(name[index] + ', ' + str(age[index]) + ' years, ' + str(height[index]) + ' hands')
