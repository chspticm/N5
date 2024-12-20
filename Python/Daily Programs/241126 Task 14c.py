# Task 14c:
# Create another quiz program, although this time, all the questions and
# answers are stored in 2 separate arrays. The program should then use a loop to ask
# each question from the array and check the answers. The program should keep a
# score and display that score to the user at the end of the program.

question = ['' for x in range(5)]
answer = ['' for x in range(5)]
question[0] = "What is the capital of the UK?"
answer[0] = 'London'
question[1] = "What is the capital of the USA?"
answer[1] = 'Washington DC'

for x in range(2):
    print(question[x])
    guess = input('>')
    if guess == answer[x]:
        print('Well Done')

# Not complete finish this program yourselves