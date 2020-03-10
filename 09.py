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

print('POO herencia')

class electrodomestico:
    def __init__(self):
        self.__isOn = False
        self.__tension = 0
    def setOn(self):
        self.__isOn = True
    def setOff(self):
        self.__isOn = False
    def isOn(self):
        return self.__isOn
    def setTension(self,tension):
        self.__tension = tension
    def getTension(self):
        return self.__tension

class lavadora(electrodomestico):
    def __init__(self):
        self.__rpm = 0
        self.__kgs = 0
    def setRpm(self,rpm):
        self.__rpm = rpm
    def setKg(self,kg):
        self.__kgs = kg
    def showStatus(self):
        print('#####')
        print('Lavadora:')
        print('\tRPM:',self.__rpm)
        print('\tKg´s:',self.__kgs)
        print('\tTensión:',self.getTension())
        if self.isOn():
            print('Encendida')
        else :
            print('Apagada')
        print('#####')

class wear:
    def __init__(self):
        self.__color = 'Blue'
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color

class secadora(electrodomestico,wear):
    def __init__(self):
        self.__turbo = False
    def checkTurbo(self):
        return self.__turbo
    def turboOn(self):
        self.__turbo = True

lavadora = lavadora()
lavadora.setRpm(3000)
lavadora.setKg(6)
lavadora.setTension(240)
lavadora.setOn()
lavadora.showStatus()

secadora = secadora()
secadora.setTension(180)
secadora.turboOn()
if secadora.checkTurbo():
    print('Turbo activado')
print('Tensión de la secadora:',secadora.getTension())
secadora.setColor('Azul')
print('Color de la ropa:',secadora.getColor())

