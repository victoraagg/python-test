print('Ejercicio de condicionales')
value1 = int(34)
value2 = int(29)
if value1<value2:
    print('El numero value1 es menor')
elif value1==value2:
    print('El numero value1 es igual a value2')
else:
    print('El numero value1 es mayor')
print('Ejercicio de bucles')
i = 0
while i<=10:
    print(i)
    i = i+1
lista = ['manzana','pera','sandia']
for var in lista:
    print(var)
for item1 in range(3):
    for item2 in range (2):
        print('Elemento1:',item1,'Elemento2:',item2)
