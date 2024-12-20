# Mr Stratton
# 31/05/2023
# Programming Challenges 18
# SQA Computing Science National 4

print('Please enter the test speed (mph).')
speed = float(input('>'))
print('Please enter the tested stopping distance (m)')
distance = float(input('>'))

passed = False

if speed == 20 and distance <= 6:
    passed = True

if speed == 30 and distance <= 14:
    passed = True

if speed == 40 and distance <= 24:
    passed = True

if speed == 50 and distance <= 38:
    passed = True

if speed == 60 and distance <= 55:
    passed = True

if speed == 70 and distance <= 75:
    passed = True



if passed:
    print('Your car passed the braking distance test')
else:
    print('Your car failed the braking distance test.')
    print('Submit your car for a tyre and brake test soon.')
