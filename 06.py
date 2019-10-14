def esNum(num):
    try:
        float(num)
        return True
    except:
        return False
    
base = input("Base triángulo: ")
while not esNum(base):
    print("El dato no es un número")
    base = input("Base triángulo: ")
    
altura = input("Altura triángulo: ")
while not esNum(altura):
    print("El dato no es un número")
    altura = input("Base triángulo: ")

baseCast = float(base)
alturaCast = float(altura)

area = baseCast * alturaCast / 2
print("Superficie triángulo:",round(area, 2))