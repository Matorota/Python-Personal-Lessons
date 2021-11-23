import turtle
import time
import winsound
from look_block import Grid
from look import Shape

# sound should work maybe
winsound.PlaySound("Tetris.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS) # leidzia garsa leisti bacgrounde (jau neleidzia)

look = Grid()
shape = Shape()
wn = turtle.Screen()
wn.title("TETRIS")
wn.bgcolor("Cornsilk")
wn.setup(width=600, height=800)
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

delay = 0.1
# win_delay = 4
score = 0

def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110

    colors = ["black", "DarkGreen", "blue", "DarkMagenta", "DarkGoldenRod", "green", "purple", "red", "SlateGray"]

    #colors duh
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 22)
            screen_y = top - (y * 22)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()


#grid checker adds score when a line is full
def check_grid(grid):
    y = 23
    while y > 0:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        if is_full:
            global score
            score += 10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y - 1][copy_x]



# def win_screen(score):
#     win = turtle.Screen()
#     win.bgcolor("black")
#     win.setup(Height=800, length=500)
#     win.title("setup")
#     win.write("You WON!!! \n Your score is: {}".format(score), move=True, align="left", font=("Arial", 24, "normal"))

def draw_score(pen, score):
    pen.color("blue")
    pen.hideturtle()
    pen.goto(20, 320)
    if(score < 100):
        pen.write("       You need 100 points to win!!! \nThe game will be paused when you win\n             "
                  "         Score: {}".format(score), move=False, align="center", font=("Arial", 18, "normal")) # siaubiakas
    else:
        print("You WON!!!")
        turtle.done()


look.grid[shape.y][shape.x] = shape.color

# key movements
wn.listen()
wn.onkeypress(lambda: shape.move_left(look.grid), "a")
wn.onkeypress(lambda: shape.move_right(look.grid), "d")
wn.onkeypress(lambda: shape.rotate(look.grid), "space")


draw_score(pen, score)

# runs game
while True:
    wn.update()

    if shape.y == 23 - shape.height + 1:
        shape = Shape()
        check_grid(look.grid)
    elif shape.can_move(look.grid):
        shape.erase_shape(look.grid)

        shape.y += 1

        shape.draw_shape(look.grid)

    else:
        shape = Shape()
        check_grid(look.grid)

    draw_grid(pen, look.grid)
    draw_score(pen, score)

    time.sleep(delay)
wn.mainloop()
