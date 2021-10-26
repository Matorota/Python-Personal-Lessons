from turtle import Turtle
star_pos = (0, -280)
move_distance = 10
finnish_line = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_position()

    def go_to_position(self):
        self.goto(star_pos)

    def up(self):
        self.forward(move_distance)

    def is_at_finnish(self):
        if self.ycor()> finnish_line:
            return True
        else:
            return False
