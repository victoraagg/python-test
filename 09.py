print('POO avanzado')

class compPrivados:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,x):
        self.__x = x
    def setY(self,y):
        self.__y = y
    def __suma(self):
        result = self.__x + self.__y
        return result
    def getResultado(self):
        return self.__suma()

x = compPrivados(12,43)
print(x.getX())
print(x.getY())
x.setX(678)
print(x.getX())
x.setY(1678)
print(x.getY())
print(x.getResultado())
