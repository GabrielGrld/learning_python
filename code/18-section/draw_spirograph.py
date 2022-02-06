import turtle as t
import random

tim = t.Turtle()

jimmy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


jimmy.shape("turtle")
jimmy.color("DeepSkyBlue", "LawnGreen")


jimmy.speed(0)
jimmy.pensize(1)


def draw_spirograph(size_of_gap, circle_radius):
    for degree in range(0, 360, size_of_gap):
        jimmy.color(random_color())
        jimmy.seth(degree)
        jimmy.circle(circle_radius)


draw_spirograph(10, 50)

screen = t.Screen()
screen.exitonclick()
