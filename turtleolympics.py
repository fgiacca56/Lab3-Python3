#turtle olympics
PI = 3.14159
radius = 30
radius = int(radius)
circumference = 2 * PI * radius

import turtle
fran = turtle.Turtle()
fran.color("blue")
fran.width(2)

def olympics():
    for i in range(30):
        fran.forward(circumference//30)
        fran.left(360//30)
olympics()
    
fran.up()
fran.forward(10)
fran.down()
fran.color("yellow")
fran.right(90)

olympics()

fran.up()
fran.left(90)
fran.forward(60)
fran.down()
fran.color("black")

olympics()

fran.up()
fran.forward(8)
fran.color("green")
fran.right(90)
fran.down()

olympics()

fran.up()
fran.left(90)
fran.forward(60)
fran.down()
fran.color("red")

olympics()





