# Mr Stratton
# 25/05/2023
# Programming Challenges 10
# SQA Computing Science National 4

print('How many par 3 holes are there?')
par3 = int(input('>'))
print('How many par 4 holes are there?')
par4 = int(input('>'))
print('How many par 5 holes are there?')
par5 = int(input('>'))
print('What is the difficulty adjustment for the course?')
diff = int(input('>'))

total = (par3 * 3) + (par4 * 4) + (par5 *5) + diff

print('The Standard Scratch for the course is:')
print(total)

