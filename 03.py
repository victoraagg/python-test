fin = False
print('Calculadora')
print('Opciones:')
print('1 - Suma')
print('2 - Resta')
print('3 - Multiplicación')
print('4 - Division')
print('5 - Salir')
while fin == False:
    option = int(input('Opción: '))
    if option == 1:
        number1 = int(input('Numero 1: '))
        number2 = int(input('Numero 2: '))
        print('Resultado:',number1+number2)
    elif option == 2:
        number1 = int(input('Numero 1: '))
        number2 = int(input('Numero 2: '))
        print('Resultado:',number1-number2)
    elif option == 3:
        number1 = int(input('Numero 1: '))
        number2 = int(input('Numero 2: '))
        print('Resultado:',number1*number2)
    elif option == 4:
        number1 = int(input('Numero 1: '))
        number2 = int(input('Numero 2: '))
        print('Resultado:',number1/number2)
    elif option == 5:
        fin = True
        print('Fin de operaciones')
