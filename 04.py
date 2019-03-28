import turtle

def makeSquare(size):
    myTurtle.forward(size)
    myTurtle.left(90)
    myTurtle.forward(size)
    myTurtle.left(90)
    myTurtle.forward(size)
    myTurtle.left(90)
    myTurtle.forward(size)
    myTurtle.left(90)
    return size

myTurtle = turtle.Turtle()

square1 = makeSquare(20)
print("Drawed square size", square1)
myTurtle.left(90)
square2 = makeSquare(30)
print("Drawed square size", square2)
myTurtle.left(90)
square3 = makeSquare(40)
print("Drawed square size", square3)
myTurtle.left(90)
square4 = makeSquare(50)
print("Drawed square size", square4)