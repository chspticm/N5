# Mr Stratton
# 30/05/2023
# Programming Challenges 16

print('Rectangle 1')
print("Please enter the following values in cm.")
print("Please enter the length")
length1 = int(input(">"))
print("Please enter the width")
width1 = int(input(">"))

area1 = length1 * width1

print('Rectangle 2')
print("Please enter the following values in cm.")
print("Please enter the length")
length2 = int(input(">"))
print("Please enter the width")
width2 = int(input(">"))

area2 = length2 * width2

if area1 > area2:
    print('Rectangle 1 has the largest area')

if area2 > area1:
    print('Rectangle 2 has the largest area')
