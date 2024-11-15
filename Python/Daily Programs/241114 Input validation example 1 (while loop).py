# RECEIVE number FROM KEYBOARD
# WHILE number < 10 OR number > 20 DO
# 	SEND “Error, please enter again” TO DISPLAY
# 	RECEIVE number FROM KEYBOARD
# END WHILE

print('Please enter a number')
number = int(input('>'))
while number < 10 or number > 20:
    print('Error, please enter again (10-20)')
    print('Please enter a number')
    number = int(input('>'))