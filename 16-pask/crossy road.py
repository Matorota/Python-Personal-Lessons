from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # kad nerenderintu automatiskai(refreshintu)

player = Player()
car_manager = CarManager()

screen.listen() # mygtuko paspaudimas
screen.onkey(player.go_forward, "Up") # mygtuko paspaudimas
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20: # cia 20 yra pixeliu, lygina atstuma tarp atskiru caru ir playerio
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish():
        car_manager.level_up()
        player.go_to_start_position()
        scoreboard.increase_level()


screen.exitonclick()