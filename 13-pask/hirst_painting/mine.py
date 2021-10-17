import colorgram
from turtle import Turtle, Screen
import random
import turtle

# pirmas etapas with colorgram got colors from img
# colors = colorgram.extract('image.jpg', 8)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#     # rgb = color.rg
#     # rgb_colors.append(rgb)
#
#
# print(rgb_colors)
#
#
#
# first_color = colors[0]
# rgb = first_color.rgb
# print(rgb)
#
tur = Turtle()

# antras

color_list =[(248, 248, 246), (247, 232, 241), (227, 238, 247), (235, 247, 242), (238, 224, 81), (205, 4, 74), (199, 164, 8), (238, 48, 132), (206, 75, 12), (109, 180, 219)]



turtle.colormode(255)

def random_color():
    num = random.randint(0, 6)
    co = color_list[num]
    return co

def dots():
    for dot in range(10):
        tur.pencolor(random_color())
        tur.dot(20)
        tur.penup()
        tur.fd(50)

tur.shape("turtle")
tur.penup()
i = -200
for dot in range(10):
    tur.setposition(-200, i)
    dots()
    i += 50

tur.hideturtle()


screen = Screen()
screen.exitonclick()