from turtle import Turtle
STARTING_POSITION = (0, -280)
TURTLE_SPEED = 10
FINISH_LINE_Y_CORD = 280


class Player(Turtle): # tai klausteliuose klasei
    def __init__(self):
        super().__init__() # leidzia klasei paduoti siuos kintamus
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start_position()

    def go_to_start_position(self):
        self.goto(STARTING_POSITION)

    def go_forward(self):
        self.forward(TURTLE_SPEED)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y_CORD:
            return True
        else:
            return False