print('Manejo de excepciones')

try:
    #print(3/'ads')
    print(3/0)
except ZeroDivisionError:
    print('Error: División entre cero')
except TypeError:
    print('Error: División entre un string')
except:
    print('Error: División errónea')
else:
    print('Divisón correcta')
finally:
    print('Salir del programa')
