print('Ejercicio de POO')
class coords:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
    def mostrarPunto(self):
        print('La coordenada es: (',self.X,',',self.Y,')')
p1 = coords(4,5)
p1.mostrarPunto()
p1.Y = 45
p1.mostrarPunto()
class triangulo:
    def __init__(self,x,y,z):
        self.X = x
        self.Y = y
        self.Z = z
    def mostrarVertices(self):
        print('Las coordenadas del triángulo son:')
        print('Coordenada X:')
        self.X.mostrarPunto()
        print('Coordenada Y:')
        self.Y.mostrarPunto()
        print('Coordenada Z:')
        self.Z.mostrarPunto()
p2 = coords(13,19)
p3 = coords(34,35)
triangle = triangulo(p1,p2,p3)
triangle.mostrarVertices()
