from turtle import Turtle, Screen
import random as rand
from player import Player
from car_manager import Enemy
import time
from scoreboard import Scoreboard

is_race_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
car_manager = Enemy()
screen.onkey(key="Up", fun=player.up)



while is_race_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_race_on = False
            scoreboard.game_over()

    if player.is_at_finnish():
        car_manager.Level_up()
        player.go_to_position()
        scoreboard.increase_level()




screen.exitonclick()
