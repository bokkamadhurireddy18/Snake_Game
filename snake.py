import time
from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # we need to move 3rd square to 2nd's position, 2nd to 1st's
            # because at turnings we turn only first square, 2nd and 3rd should follow 1st square
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)