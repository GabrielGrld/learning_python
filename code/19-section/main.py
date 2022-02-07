from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(30)


def move_backwards():
    tim.backward(30)


def turn_right():
    actual_heading = tim.heading()
    new_heading = actual_heading - 10
    tim.seth(new_heading)


def turn_left():
    actual_heading = tim.heading()
    new_heading = actual_heading + 10
    tim.seth(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
