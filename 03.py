print('Proyecto de calculadora')

fin = False
print('Calculadora')
print('Opciones:')
print('1 - Suma')
print('2 - Resta')
print('3 - Multiplicación')
print('4 - Division')
print('5 - Salir')

def readNum(text):
    valid = False
    while not valid:
        try:
            number = int(input(text))
        except ValueError:
            print('El valor debe ser un número')
        else:
            valid = True
    return number

while fin == False:
    option = int(input('Opción: '))
    if option == 1:
        number1 = readNum('Numero 1: ')
        number2 = readNum('Numero 2: ')
        print('Resultado:',number1+number2)
    elif option == 2:
        number1 = readNum('Numero 1: ')
        number2 = readNum('Numero 2: ')
        print('Resultado:',number1-number2)
    elif option == 3:
        number1 = readNum('Numero 1: ')
        number2 = readNum('Numero 2: ')
        print('Resultado:',number1*number2)
    elif option == 4:
        number1 = readNum('Numero 1: ')
        number2 = readNum('Numero 2: ')
        try:
            result = number1/number2
        except ZeroDivisionError:
            print('División entre cero')
        except:
            print('Error en la división')
        else:
            print('Resultado:',result)
    elif option == 5:
        fin = True
        print('Fin de operaciones')
