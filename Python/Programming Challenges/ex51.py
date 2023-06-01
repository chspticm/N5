# Mr Stratton
# 25/05/2023
# Programming Challenges 51
# SQA Computing Science National 5

print('Enter the area in m\N{SUPERSCRIPT TWO} to be painted.')
area = int(input('>'))
print('Enter the area in m\N{SUPERSCRIPT TWO} that a single pot covers.')
pot = int(input('>'))

needed = area / pot

if needed == int(needed):
    print('You will need', int(needed), 'pots of paint.')
else:
    leftOver = area % pot
    print('You will need', int(needed) + 1, 'pots of paint.')
    print('You can paint', leftOver, 'm\N{SUPERSCRIPT TWO} with the left over paint.')