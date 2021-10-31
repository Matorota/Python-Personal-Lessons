from turtle import Screen
from player import Player
import turtle
import random
import time

screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('turquoise')

player = Player()

screen.listen() # mygtuko paspaudimas
screen.onkey(player.go_forward, "Up") # mygtuko paspaudimas

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
