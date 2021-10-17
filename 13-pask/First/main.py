import turtle as t
import random as rand

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)

tim.shape("turtle")


# tim.color("green")


def random_color():
    r = rand(0, 255)
    g = rand(0, 255)
    b = rand(0, 255)
    color = (r, g, b)
    return color


def draw_square(size): # nupiesia kvadrata
    for _ in range(4):
        tim.forward(size)
        tim.left(90)


def draw_dash(dash_size, dashes):
    for i in range(dashes):
        tim.forward(dash_size)
        tim.penup()
        tim.forward(dash_size)
        tim.pendown()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def draw_spirograpth(radius, size_of_gap):
    tim.speed("fastest")
    for angle in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap)


tim.color(random_color())
#draw_square(40) #piesimo dalis
#draw_dash(10, 5)
# for shape_side in range(3, 11):
#     draw_shape(shape_side)
draw_spirograpth(100, 5)


screen.exitonclick() #neleidzi iskartp uzsidaryti

