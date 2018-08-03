import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

def arm(color):
    t.pendown()
    t.begin_fill()
    t.color(color)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.setheading(0)

t.speed('fastest')
t.bgcolor('Dodger blue')
t.shape('turtle')
# feet

t.goto(-100, -150)
rectangle(50, 20, 'navy')
t.goto(-30, -150)
rectangle(50, 20, 'navy')
t.goto(-25, -50)
# legs

rectangle(15, 100, 'turquoise')
t.goto(-55, -50)
rectangle(-15, 100, 'turquoise')
t.goto(-90, 100)
# body

rectangle(100, 150, 'purple')
# arms

t.goto(-90, 80)
t.setheading(135)
arm('turquoise')

t.goto(10, 80)
t.setheading(315)
arm('turquoise')
#neck

t.goto(-50, 120)
rectangle(15, 20, 'navy')
# head

t.goto(-85, 170)
rectangle(80, 50, 'green')
# eyes

t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')
# mouth

t.goto(-65, 135)
rectangle(40, 5, 'black')

t.hideturtle()
t.mainloop()