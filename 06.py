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
        print('- LIBRO --')
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

biblioteca = biblioteca()
print(biblioteca.countLibros())
