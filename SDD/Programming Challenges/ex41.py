# Mr Stratton
# 01/06/2023
# Programming Challenges 41
# SQA Computing Science National 5

score = [0 for x in range(6)]
total = 0

print('Please enter the score for each ball.')
for x in range(6):
    score[x] = int(input('>'))
    total = total + score[x]

print("This over's score was:", total)
print('With each ball scoring:')
for x in range(6):
    print(score[x])
