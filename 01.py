print("Hola mundo")
print("Ejercicio de variables y strings")
name = input('Nombre: ')
print('Hola,',name.capitalize())
print('Hola,',name.upper())
print("Ejercicio de ints")
age = int(input('Indica tu edad: '))
fav = int(input('Indica tu número preferido: '))
print('Resultado:',age+fav)
result = age < fav
print('¿Es menor age que fav?',result)
print("Ejercicio de listas")
lista = ['manzana','pera','sandia']
print(lista)
position = int(input('¿Que posición de la lista quieres eliminar? '))
del lista[position]
print(lista)
stringsepare = input('Cadena para separar: ')
print(stringsepare.split())
