x = input("Numero 1: ")
y = input("Numero 2: ")
isValidx = False
isValidy = False

while not isValidx and not isValidy:
    if x.isdigit() == False:
        print("El valor", x, "no es un entero")
        x = input("Numero 1: ")
    else:
        isValidx = True
    if y.isdigit() == False:
        print("El valor", y, "no es un entero")
        y = input("Numero 2: ")
    else:
        isValidy = True

x = int(x)/10
y = int(y)/10

print("Suma de ambos: ", round(x+y,2))
print("Resta de ambos: ", round(x-y,2))
print("Multiplicacion de ambos: ", round(x*y,2))
print("Division de ambos: ", round(x/y,2)) 
