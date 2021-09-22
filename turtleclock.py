import turtle

fran = turtle.Turtle()
fran.shape("turtle")


def turtle_clock():
    for i in range(1):
        fran.up()
        fran.forward(75)
        fran.down()
        fran.forward(25)
        fran.up()
        fran.forward(25)
        fran.stamp()


def turtle_clock2():
    for i in range(1):
        fran.up()
        fran.backward(125)
        fran.right(30)

for i in range(12):
    part1 = turtle_clock()
    part2 = turtle_clock2()
 
