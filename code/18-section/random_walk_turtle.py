import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
orientation = [0, 90, 180, 270]

jimmy = t.Turtle()
jimmy.shape("turtle")
jimmy.color("DeepSkyBlue", "LawnGreen")

steps = int(input("Step to graph: "))
steps_length = int(input("Step Length: "))
jimmy.speed(0)
jimmy.pensize(10)


def random_walk(_steps, _steps_length):
    for side in range(1, _steps+1):
        jimmy.color(random.choice(colours))
        jimmy.seth(random.choice(orientation))
        jimmy.forward(_steps_length)

random_walk(steps, steps_length)




