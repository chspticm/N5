# Mr Stratton
# 01/06/2023
# Programming Challenges 45
# SQA Computing Science National 5

name = ['Mellisa', 'Evelyn', 'Emmy', 'Karen', 'Margaret', 'Norma', 'Agnes', 'Billy', 'Robert', 'Arthur']
attending = [False for x in range(10)]

print('Who\'s going?')
for index in range(10):
    print(name[index] + '?')
    answer = input('>')
    if answer == 'Y' or answer == 'y':
        attending[index] = True

print('\nParty List:')
for x in range(10):
    if attending[x]:
        print(name[x])