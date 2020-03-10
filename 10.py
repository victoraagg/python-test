print('Operaciones con ficheros')

file = open('./files/test.txt','r')
texto = file.read()
file.close
print(texto)
print('###')

file = open('./files/test.txt','r')
textoArray = file.readlines()
file.close
print(textoArray[1])
print('###')

file = open('./files/test.txt','a')
nuevaLinea = file.write('Nueva línea añadida\n')
file.close
print(texto)
print('###')

file = open('./files/test.txt','r')
texto = file.read()
file.close
print(texto)
print('###')
