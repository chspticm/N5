# Mr Stratton
# 31/05/2023
# Programming Challenges 34
# SQA Computing Science National 4

print('Please enter the test speed (mph).')
speed = float(input('>'))
while speed < 20:
    print('Sorry, must be 20 or more. Enter again.')
    print('Please enter the test speed (mph).')
    speed = float(input('>'))

print('Please enter the tested stopping distance (m)')
distance = float(input('>'))
while distance <= 0 :
    print('Sorry, please enter a value greater than 0')
    print('Please enter the tested stopping distance (m)')
    distance = float(input('>'))

if (speed == 20 and distance <= 6) or (speed == 30 and distance <= 14) or (speed == 40 and distance <= 24) or (speed == 50 and distance <= 38) or (speed == 60 and distance <= 55) or (speed == 70 and distance <= 75):
    passed = True
else:
    passed = False

if passed:
    print('Your car passed the braking distance test')
    print('Well done')
else:
    print('Your car failed the braking distance test.')
    print('Submit your car for a tyre and brake test soon.')
