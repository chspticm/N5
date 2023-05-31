# Mr Stratton
# 31/05/2023
# Programming Challenges 25
# SQA Computing Science National 4

total = 0

print('Please enter the seven temperatures')
for loop in range(7):
    temp = int(input('>'))
    total = total + temp

average = total / 7

print('This week\'s average was:')
print(round(average,2),'degrees centigrade')