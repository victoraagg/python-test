key = 1
y = 0
while key <= 100:
    y = y+key
    print(y, ' - Posición:', key)
    key = key+1
    
totalCounter = 0
for counter in range(1,101):
    totalCounter = totalCounter + counter
    
print('Suma total en bucle for:', totalCounter)