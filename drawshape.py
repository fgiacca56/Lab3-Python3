import turtle
fran = turtle.Turtle()
n = int(input("Please enter the number of sides desired:"))

angles = 360/n
        
for i in range(n):
        draw = fran.forward(50)
        angle = fran.right(angles)
        
