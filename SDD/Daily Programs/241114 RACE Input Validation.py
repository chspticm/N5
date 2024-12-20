# Input validation
# only allow the user to enter a number between 4 and 6
# Using RACE Input Validation (Repeat Ask Check Error)

while True: # Repeat
    print('Please enter a number')  # Ask
    number = float(input('>'))
    if number < 4 or number > 6: # Check
        print('The number must be between 4 and 6') # Error
    else:
        break
    
