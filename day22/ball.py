from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.recent_bounce = False  # New variable to track recent bounces

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        self.recent_bounce = True  # Set recent bounce flag

    def reset_position(self):
        import time
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
        self.recent_bounce = False



