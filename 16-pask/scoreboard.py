from turtle import Turtle
STYLE = ("roboto", 10, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() # leidzia visus siuos elementus perduotis kitiems
        self.level =1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard

    def update_scorevoard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=STYLE)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!!! {self.level}", align="left", font=STYLE)

    def increse_level(self):
        self.level += 1
        self. update_scorevoard()
