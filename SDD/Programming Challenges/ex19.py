# Mr Stratton
# 31/05/2023
# Programming Challenges 19
# SQA Computing Science National 5

print("Please enter the current temperature (C)")
temp = int(input('>'))

print('At',temp,'degrees centigrade')
if temp <= 0:
    print('Water will be a solid')
elif temp >= 100:
    print('Water will be a gas')
else:
    print('Water will be a liquid')
