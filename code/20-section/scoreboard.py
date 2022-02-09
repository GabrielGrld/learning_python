from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.score = 0
        self.goto(0, 250)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", True, align=ALIGNMENT, font=FONT)
        self.goto(0, 250)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
