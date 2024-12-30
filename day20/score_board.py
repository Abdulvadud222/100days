from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.scores}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=-60, y=0 )
        self.write("GAME OVER!", font=FONT)


    def increase_score(self):
        self.scores += 1
        self.update_score()






