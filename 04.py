print('Ejercicio de funciones')
def saludar():
    print('Hola a todos')
saludar()
def esMayorQueCero(value):
    if int(value) < 0:
        return value+' es mayor que cero'
    else:
        return value+' es menor que cero'
number = input('Introduce un número: ')
print(esMayorQueCero(number))
def funcionesDosReturn(value):
    cuadrado = value * value
    cubo = value * value * value
    return cuadrado,cubo
arit = int(input('Introduce un número: '))
cuadrado,cubo = funcionesDosReturn(arit)
print('El cuadrado de',arit,'es:',cuadrado,'Su cubo es:',cubo)
name = input('Nombre: ')
def toUpperCase(string):
    return string.upper()
def saludaNombre(name):
    print('Hola, soy',toUpperCase(name))
saludaNombre(name)
