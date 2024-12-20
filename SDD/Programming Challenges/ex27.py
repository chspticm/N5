# Mr Stratton
# 31/05/2023
# Programming Challenges 27
# SQA Computing Science National 4 (5)

total =0 

print('How many charity raisers were there?')
raisers = int(input('>'))

print('Enter the total raised by each:')
for x in range(raisers):
    raised = int(input('>'))
    total = total + raised

print('A total of £' + str(total),'was raised.')

if total < 1000:
    total = total + 100
elif total >= 1000 and total < 2000:
    total = total * 2
elif total > 2000:
    total = 4000 + (total - 2000)
else:
    print('An error has occurred')
    
print('With the company bonus, this will be')
for x in range(3):
     print('£' + str(total) + '!!!')

