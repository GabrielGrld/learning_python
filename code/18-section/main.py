# import turtle
# tim = turtle.Turtle()

# from turtle import Turtle
#
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()


import turtle as t
# tim = t.Turtle()



from turtle import Turtle, Screen
import random

colours = ["cyan", "purple", "white", "blue"]

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("DeepSkyBlue", "LawnGreen")

sides = int(input("Sides to graph: "))
side_length = int(input("Side Length: "))


def draw_figure(side):
    for side in range(1, side+1):
        jimmy.forward(side_length)
        jimmy.right(360/x)
    jimmy.seth(0)


for x in range(3, sides+1):
    draw_figure(x)
    jimmy.color(random.choice(colours))





























screen = Screen()
screen.exitonclick()