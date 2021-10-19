from turtle import Turtle, Screen
import random as rand

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = [item for item in input("parasyk spalvas max 6 ir i viena eil: ").split()]
user_bet = screen.textinput(title="Kas laimes?", prompt="ok pog? spalva (tik nezydra) ")
print("pick a number color")
for retry in range(5):
    if user_bet == colors:
        print("all good")
        break
    print("you have made an invalid choice, try again.")
else:
    print("you keep making invalid choices, exiting.")


print(user_bet)

positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# turtles = 6

for players in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[players])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=positions[players])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = rand.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Laimejai!, Laimejo {winning_color} VEZLYSSS.")
            else:
                print(f"praradai pinigus!, Tavo pinigus turi {winning_color} VEZLYSSS.")


screen.exitonclick()

