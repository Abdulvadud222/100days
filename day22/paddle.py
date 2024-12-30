from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5.0, 1.0, 0.0)
        self.goto(position)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.sety(new_y)
