from turtle import Turtle
import random as rand

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_speed = 5
movement = 10
positions = []


class Enemy(Turtle):

    def __init__(self, ):
        self.cars = []
        self.car_speed = starting_speed

    def add_car(self):
        random_chance = rand.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.colors(rand.choice(colors))
            random_y = rand.randint(-250, 250)
            new_car.goto(300, y)
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self):
        for enemy in self.cars:
            if enemy.xcor() < -320:
                enemy.hideturtle()
                self.cars.remove(enemy)
            else:
                enemy.forward(self.start_move)

    def level_up(self):
        self.start_move += movement
        self.Add += 1

    def reset(self):
        self.start_move = 5
        self.Add = 1


