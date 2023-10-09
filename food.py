from turtle import Turtle
import random
import snake

SIZE = 0.6


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_wid=SIZE, stretch_len=SIZE)
        self.speed("fastest")
        self.place()

    def place(self):
        random_x = random.randint(-13, 13) * snake.CELL_SIZE
        random_y = random.randint(-13, 13) * snake.CELL_SIZE
        self.goto(x=random_x, y=random_y)
