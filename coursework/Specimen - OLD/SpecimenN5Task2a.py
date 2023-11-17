# N5 Specimen Task 2a
# Mr Stratton
# 12/06/2023

hits = [0 for x in range(6)]
average = 0.0
totalHits = 0
points = 0

for index in range(6):
    print('Please enter the score for player', index + 1)
    hits[index] = int(input('>'))
    while hits[index] < 0 or hits[index] > 30:
        print('The number of hits a single player can achieve is greater than or equal to 0 and less than or equal to 30')
        print('Please enter the score for player', index + 1)
        hits[index] = int(input('>'))

for index in range(6):
    totalHits = totalHits + hits[index]

average = totalHits / 6

average = round(average, 2)

if totalHits > 50:
    points = points + 1

if average >= 10:
    points = points + 1

if points == 1:
    print('1 point was earned')

if points == 2:
    print('An additional point was earned')

if points == 0:
    print('No points were earned')
