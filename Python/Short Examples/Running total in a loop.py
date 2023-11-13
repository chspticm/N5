# Standard Algorithm 
# Running total in a fixed loop

print('How many prices to add?')
prices = int(input('>'))

total = 0

for loop in range(prices):
    print('Please the enter price of item', loop + 1)
    price = float(input('£'))
    total = total + price

print('The total for the', prices, 'items is £', round(total,2))
