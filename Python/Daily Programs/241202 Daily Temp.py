# Average Temp
# 2/12/24
# Mr Stratton

temp = [0.0 for x in range(7)]
total = 0
 
for x in range(7):
    print('What is the temperature for day',x+1)
    temp[x] = float(input('>'))
    total = total + temp[x]
     
print('The average temperature for the week is', round(total/7,1))
