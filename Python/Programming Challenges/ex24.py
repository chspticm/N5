# Mr Stratton
# 31/05/2023
# Programming Challenges 24
# SQA Computing Science National 4

total = 0

print('Please enter the score for each ball.')
for x in range(6):
    score = int(input('>'))
    total = total + score

print("This over's score was:", total)
