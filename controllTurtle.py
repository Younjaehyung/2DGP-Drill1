import turtle

def movew():
    turtle.forward(50)
    turtle.stamp()
def movea():
    turtle.left(90)
    turtle.forward(50)
    turtle.stamp()
def moves():
    turtle.forward(-50)
    turtle.stamp()
def moved():
    turtle.right(90)
    turtle.forward(50)
    turtle.stamp()

def esc():
   turtle.reset()
   turtle.left(90)

turtle.shape("turtle")
esc()
turtle.onkey(movew, 'w')
turtle.onkey(movea, 'a')
turtle.onkey(moves, 's')
turtle.onkey(moved, 'd')
turtle.onkey(esc,'Escape')
turtle.listen()
