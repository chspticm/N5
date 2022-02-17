# 2018 Assignment
# Solution

counter=0 #int
validReading=[0]*5 # Int Readings
reading=0.0 #real
patern="" #String

for counter in range(5):
    reading=float(input("What is the reading?"))
    while reading<0 and reading>100:
        print("Sorry please enter a value between 0 and 100")
        reading=float(input("What is the reading?"))
    
    validReading[counter]=round(reading)
    
    if validReading[counter]>80:
        patern=patern+"S"
    else:
        if validReading[counter]<30:
            patern=patern+"P"
        else:
            patern=patern+"M"

print("Signal Patern is:",patern)

for counter in range(5):
    print("Reading " + str(counter+1) + " - " + str(validReading[counter]))
    

    