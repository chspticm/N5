# Mr Stratton
# 01/06/2023
# Programming Challenges 44
# SQA Computing Science National 5

roomLength = [0.0 for x in range(10)]
roomWidth = [0.0 for x in range(10)]
total = 0

print('House floor area calculator.')
print('Please enter the number of rooms:')
rooms = int(input('>'))

for index in range(rooms):
    print('Please enter the length (m) of room', index + 1)
    roomLength[index] = float(input('>'))
    print('Please enter the width (m) of room', index + 1)
    roomWidth[index] = float(input('>'))

print('The total area is calculated as:')
for index in range(rooms):
    print('Room', index + 1)
    area = roomLength[index] * roomWidth[index]
    total = total + area
    print(roomLength[index], 'x', roomWidth[index], '=', round(area,2), 'metres squared')

print('\nTotal Area =', round(total,2), 'metres squared')