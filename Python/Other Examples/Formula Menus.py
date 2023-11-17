''' 
Write a program that allows the user to calculate the following areas
 a square
 a circle
 a rectangle
 '''
# Mr Stratton
# 17/11/23

while True:
    print('Please select the shape to calculate the are of' )
    print('A - Square')
    print('B - Circle')
    print('C - Rectangle')
    print('\nAny other selection will close the program')
    choice = input('>')
    if choice == 'A' or choice == 'a':
        print('Please enter the length of the sides')
        length = float(input('>'))
        area = length**2
        print('The area of the square was',area)
    
    elif choice == 'B' or choice == 'b':
        print('Please enter the length of the radius')
        radius = float(input('>'))
        area = 3.14 * (radius**2)
        print('The area of the circle was',area)

    elif choice == 'C' or choice == 'c':
        print('Please enter the length of the rectangle')
        length = float(input('>'))
        print('Please enter the breadth of the rectangle')
        breadth = float(input('>'))
        area = length * breadth
        print('The area of the rectangle was',area)

    else:
        break

    print('\n')
