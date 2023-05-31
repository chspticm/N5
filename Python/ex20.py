# Mr Stratton
# 31/05/2023
# Programming Challenges 19
# SQA Computing Science National 5


print('Please enter the first amount raised.')
first = int(input('>'))
print('Please enter the second amount raised.')
second = int(input('>'))
print('Please enter the third amount raised.')
third = int(input('>'))

total = first + second + third

print('A total of £' + str(total),'was raised.')

if total < 1000:
    total = total + 100
elif total >= 1000 and total < 2000:
    total = total * 2
elif total > 2000:
    total = 4000 + (total-2000)
else:
    print('An error has occured')
    
print('With the company bonus, this will be £' + str(total))

