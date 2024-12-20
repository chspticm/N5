# 1 initialise variables
# 2 get valid training session duration
print('What is the duration of the training session?')
duration = int(input('>'))
while duration <10 or duration >30:
    print('Error, the number must be between 10 and 30')
    print('What is the duration of the training session?')
    duration = int(input('>'))
# 3 convert duration of training session to seconds
duration = duration * 60
# 4 calculate total duration of songs
#START HERE
# 5 display training session summary