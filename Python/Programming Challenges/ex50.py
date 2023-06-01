# Mr Stratton
# 01/06/2023
# Programming Challenges 50
# SQA Computing Science National 5

print("Please enter the 1st set of letters")
firstLetters = input(">").upper()
print("Please enter the 1st set of numbers")
firstNumber = input(">")
print("Please enter the 2nd set of numbers")
secondNumber = input(">")
print("Please enter the 2nd set of letters")
secondLetters = input(">").upper()

postcode = firstLetters + firstNumber + " " + secondNumber + secondLetters

print(postcode)

if len(postcode) > 8:
    print('Sorry - Postcode is longer than 8 characters')
