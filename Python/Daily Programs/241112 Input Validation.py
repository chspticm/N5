# Mr Stratton
# 12/11/24
# Input Validation

# Write a program that allows the user to only enter the numbers 1 to 10.

# 1.	Ask the user to enter a number
print('Please enter a number between 1 and 10')
number = int(input('>'))
# 2.	Repeat While number not between 1 and 10
while number < 1 or number > 10:
# 3.		Display “Error, number not between 1 and 10”
    print('Error, number is not between 1 and 10')
# 4.		Ask the user to enter a number
    print('Please enter a number between 1 and 10')
    number = int(input('>'))
# 5.	End Repeat
