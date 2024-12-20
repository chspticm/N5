# Input Validation 
# RACE

while True: # Repeat
    print('Please enter a number between 1 and 6') # Ask
    number = int(input('>'))

    if number < 1 or number > 6: # Check
        print('Error! Make sure the number is between 1 and 6')  # Error
    else:
        break # Exit

print('The number is', number)