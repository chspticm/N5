# 2023 Task 1b
# Mr Stratton
# 03/12/24

# Set up arrays and variables
journeyStage = [0.0 for x in range(10)]
milesTravelled = [0 for x in range(10)]
totalJourneyCost = 0
totalMiles = 0

# Get Journey Details
print('What is the start milage?')
startMiles = int(input('>'))
print('How many charging stations did you use?')
stations = int(input('>'))

# Calculate and store the cost of each stage of the journey
for x in range(stations):
    print("What is the mileage for station", x + 1)
    currentMiles = int(input('>'))
    print('What is the kW rating for the charging station')
    rating = int(input('>'))
    while rating != 7 and rating !=22 and rating != 50:
        print('Error, the rating must be 7, 22, or 50')
        print('What is the kW rating for the charging station')
        rating = int(input('>'))
        
    if rating == 7: # Code was not run due to wrong indentation
        pricePerMile = 0
    elif rating == 22:
        pricePerMile = 0.005
    else:
        pricePerMile = 0.01
    
    milesTravelled[x] = currentMiles - startMiles
    
    startMiles = currentMiles
    
    journeyStage[x] = pricePerMile * milesTravelled[x]
              
# Display total miles, journey stage costs and total cost
for x in range(stations):
    print('Journey Stage', x+1)
    print('Cost for stage',journeyStage[x])
    totalJourneyCost = totalJourneyCost + journeyStage[x]
    totalMiles = totalMiles + milesTravelled[x]

print('Total Journey cost = ',round(totalJourneyCost,2))
print('The total millage is',totalMiles)
    