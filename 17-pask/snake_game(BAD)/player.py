import turtle


STARTING_POSITION = (0, -280)
TURTLE_SPEED = 10
FINISH_LINE_Y_CORD = 280


class Player(turtle): # tai klausteliuose klasei
    def __init__(self):
        super().__init__() # leidzia klasei paduoti siuos kintamus
        snake = turtle.Turtle()
        snake.speed(0)
        snake.shape('square')
        snake.color("black")
        snake.penup()
        snake.goto(0, 0)
        snake.direction = 'stop'


    snake = turtle.Turtle()
    snake.speed(0)
    snake.shape('square')
    snake.color("black")
    snake.penup()
    snake.goto(0, 0)
    snake.direction = 'stop'

    fruit = turtle.Turtle()
    fruit.speed(0)
    fruit.shape('circle')
    fruit.color('red')
    fruit.penup()
    fruit.goto(30, 30)

    old_fruit = []

    scoring = turtle.Turtle()
    scoring.speed(0)
    scoring.color("black")
    scoring.penup()
    scoring.hideturtle()
    scoring.goto(0, 300)
    scoring.write("Score :", align="center", font=("Courier", 24, "bold"))

    def snake_go_up(self):
        if snake.direction != "down":
            snake.direction = "up"

    def snake_go_down():
        if snake.direction != "up":
            snake.direction = "down"

    def snake_go_left():
        if snake.direction != "right":
            snake.direction = "left"

    def snake_go_right():
        if snake.direction != "left":
            snake.direction = "right"

    def snake_move():
        if snake.direction == "up":
            y = snake.ycor()
            snake.sety(y + 20)
        if snake.direction == "down":
            y = snake.ycor()
            snake.sety(y - 20)
        if snake.direction == "left":
            x = snake.xcor()
            snake.setx(x - 20)
        if snake.direction == "right":
            x = snake.xcor()
            snake.setx(x + 20)

    screen.listen()
    screen.onkeypress(snake_go_up, "Up")
    screen.onkeypress(snake_go_down, "Down")
    screen.onkeypress(snake_go_left, "Left")
    screen.onkeypress(snake_go_right, "Right")