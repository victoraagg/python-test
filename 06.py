print('Ejercicio de POO avanzado')

class autor:
    def __init__(self,nombre,apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    def getAutor(self):
        print('Autor:',self.nombre,self.apellidos)
        
class libro:
    def __init__(self,titulo,isbn):
        self.titulo = titulo
        self.isbn = isbn
    def setAutor(self,autor):
        self.autor = autor
    def getLibro(self):
        print('########## LIBRO ##########')
        self.autor.getAutor()
        print('Título:',self.titulo)
        print('ISBN:',self.isbn)
    def getTitulo(self):
        return self.titulo

class biblioteca:
    def __init__(self):
        self.listaLibros = []
    def countLibros(self):
        return len(self.listaLibros)
    def setLibro(self,name):
        self.listaLibros = self.listaLibros + [name]
    def showBiblioteca(self):
        for libro in self.listaLibros:
            libro.getLibro()
    def unsetLibro(self,titulo):
        exists = False
        position = -1
        for libro in self.listaLibros:
            position += 1
            if libro.getTitulo() == titulo:
                exists = True
                break
        if exists:
            del self.listaLibros[position]
            print('Libro',titulo,'borrado')
        else:
            print('Libro',titulo,'no encontrado')

def showMenu():
    print('Opciones disponibles')
    print('1 - Añadir libro')
    print('2 - Mostrar biblioteca')
    print('3 - Borrar libro')
    print('4 - Mostrar numero de libros')
    print('5 - Salir')

def addBook(biblioteca):
    titulo = input('Titulo del libro: ')
    isbn = input('ISBN del libro: ')
    nombre = input('Nombre del autor: ')
    apellidos = input('Apellidos del autor: ')
    nuevoAutor = autor(nombre,apellidos)
    nuevoLibro = libro(titulo,isbn)
    nuevoLibro.setAutor(nuevoAutor)
    biblioteca.setLibro(nuevoLibro)

def showBiblioteca(biblioteca):
    biblioteca.showBiblioteca()

def borrarLibro(biblioteca):
    titulo = input('Titulo del libro a borrar: ')
    biblioteca.unsetLibro(titulo)

def numberBooks(biblioteca):
    print('Numero de libros en la biblioteca:',biblioteca.countLibros())

fin = False
biblioteca = biblioteca()

while not fin:
    showMenu()
    option = int(input('Opción: '))
    if option == 1:
        addBook(biblioteca)
    elif option == 2:
        showBiblioteca(biblioteca)
    elif option == 3:
        borrarLibro(biblioteca)
    elif option == 4:
        numberBooks(biblioteca)
    elif option == 5:
        fin = True
        print('Biblioteca cerrada')
