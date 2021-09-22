import turtle
fran = turtle.Turtle()
fran.shape("triangle")


sides = int(input("Please enter a side length"))

for i in range(sides):
    fran.forward(100)
    fran.left(360//sides)
