import turtle as t
from random import randint, random

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

def keyaction(event):
    global draw
    draw = False

# Main code
t.speed(0)
draw = True
canvas = t.getcanvas()
canvas.bind_all('<Key>', keyaction)
t.Screen().bgcolor('dark blue')

while draw:
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(10, 100)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)

t.mainloop()