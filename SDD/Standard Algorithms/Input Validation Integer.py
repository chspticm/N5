# Input Validation 
# AREA

print('Please enter a number between 1 and 6')
number = int(input('>'))

while number < 1 or number > 6:
    print('Error! Make sure the number is between 1 and 6')
    print('Please enter a number between 1 and 6')
    number = int(input('>'))

print('The number is', number)