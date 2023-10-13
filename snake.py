from turtle import Turtle

CELL_SIZE = 20
STARTING_POS = [(0, 0), (-CELL_SIZE, 0), (-CELL_SIZE * 2, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.goto(pos)
            new_segment.color("white")
            self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments)):
            if i == len(self.segments) - 1:
                self.head.forward(CELL_SIZE)
            else:
                self.segments[-i - 1].goto(x=self.segments[-i - 2].xcor(), y=self.segments[-i - 2].ycor())
                self.segments[-i - 1].showturtle()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        new_segment = Turtle(shape="square")
        new_segment.hideturtle()
        new_segment.penup()
        new_segment.color("white")
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
