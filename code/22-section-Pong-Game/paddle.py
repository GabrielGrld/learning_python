from turtle import Turtle


STARTING_POSITIONS = [(350, 50), (350, 30), (350, 10), (350, -10), (350, -20)]
MOVE_DISTANCE = 20


class Paddle:

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        new_x = self.head.xcord()
        new_y = self.head.ycord() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def down(self):
        new_x = self.head.xcord()
        new_y = self.head.ycord() - MOVE_DISTANCE
        self.goto(new_x, new_y)
