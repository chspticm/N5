# Mr Stratton
# 31/05/2023
# Programming Challenges 28
# SQA Computing Science National 4 

player1 = 0
player2 = 0

print('Please enter the scores for player one.')
for index in range(3):
    score = int(input('>'))
    player1 = player1 + score

print('Please enter the scores for player two.')
for index in range(3):
    score = int(input('>'))
    player2 = player2 + score

print('Player one scored:', player1)
print('Player two scored:', player2)
if player1 > player2:
    print('Player One Wins!')
elif player2 > player1:
    print('Player Two Wins!')
else:
    print('It\'s a draw')


