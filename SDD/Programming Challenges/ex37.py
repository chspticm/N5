# Mr Stratton
# 31/05/2023
# Programming Challenges 37
# SQA Computing Science National 5

total = 0

print('Please enter the seven temperatures')
for loop in range(7):
    temp = int(input('>'))
    while temp < -40 or temp > 55:
        print('Please enter a temperature between -40 and 55')
        temp = int(input('>'))

    total = total + temp

average = total / 7

print('This week\'s average was:')
print('rounded to 0 decimal places was:')
print(round(average), 'degrees centigrade')