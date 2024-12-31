FONT = ("Courier", 28, "normal")
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.goto(x=-240, y=265)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
