# Input Validation of a string
# AREA

print('Please enter Y or N')
choice = input('>')

while choice != 'Y' and choice != 'N':
    print('Error! Only enter Y or N')
    print('Please enter Y or N')
    choice = input('>')

print('The choice is', choice)