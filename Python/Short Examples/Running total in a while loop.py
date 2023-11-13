# Standard Algorithm 
# Running total in a conditional loop

price = -1
total = 0
item = 0

while price != 0:
    item = item + 1
    print('Please enter the price of item', item)
    print('Enter 0 to stop entering prices.')
    price = float(input('£'))

    total = total + price


print('The total for the', item - 1, 'items is £', round(total, 2))