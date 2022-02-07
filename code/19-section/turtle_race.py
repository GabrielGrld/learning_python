from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutrtle will win the race? Enter a Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -100

all_turtles = []
for color in colors:
    color_name = color
    color = Turtle(shape="turtle")
    color.color(color_name)
    color.penup()
    color.goto(-230, y_position)
    y_position += 50
    all_turtles.append(color)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()