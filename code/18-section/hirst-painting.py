# import colorgram
#
# extract most common  colors from image
# colors = colorgram.extract('image.jpg', 30)
# color_array = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     color_tuple = (r, g, b)
#     color_array.append(color_tuple)
#
# print(color_array)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


color_list = [(182, 163, 132), (144, 162, 183), (125, 98, 68), (179, 151, 164), (82, 99, 127), (123, 82, 97), (164, 151, 54), (213, 203, 140), (147, 171, 157), (63, 37, 25), (68, 24, 34), (86, 111, 92), (160, 106, 125), (32, 42, 63), (101, 122, 167), (108, 39, 57), (210, 180, 192), (177, 189, 212), (167, 111, 97), (82, 87, 20), (211, 183, 177), (105, 44, 36), (169, 204, 189), (104, 144, 118), (41, 59, 100), (38, 53, 45)]
# tim.fillcolor("blue")
# tim.color("green", "yellow")
# t.begin_fill()
t.speed(0)
t.hideturtle()

tim.penup()
tim.goto(-100, -100)
tim.pendown()


def draw_row(points, distance, circle_radius):
    for _ in range(points):
        tim.color(random.choice(color_list))
        tim.penup()
        tim.forward(distance)
        tim.pendown()
        tim.dot(circle_radius, random.choice(color_list))


for row in range(1, 11):
    draw_row(10, 20, 10)
    tim.penup()
    tim.goto(-100, -100 + row*20)
    tim.pendown()

screen = t.Screen()
screen.exitonclick()