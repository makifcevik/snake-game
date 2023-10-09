from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.speed("fastest")
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)
