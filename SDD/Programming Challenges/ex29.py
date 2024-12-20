# Mr Stratton
# 31/05/2023
# Programming Challenges 29
# SQA Computing Science National 5

total =0

print('Enter the time in seconds for each pupil.')
for x in range(1, 4):
    print('Pupil', x)
    pupilTime = int(input('>'))
    total = total + pupilTime

average = total / 3

print(round(average, 2), 'seconds')