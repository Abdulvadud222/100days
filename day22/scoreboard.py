from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 48, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 250)
        self.write(self.player1_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.player2_score, align=ALIGNMENT, font=FONT)


    def player1_point(self):
        self.player1_score += 1
        self.clear()
        self.update_scoreboard()

    def player2_point(self):
        self.player2_score += 1
        self.clear()
        self.update_scoreboard()

    def winner_player1(self):
        self.goto(150, 0)
        self.write("You win!", font=("Courier", 24, "normal"))
        self.goto(x=-250, y=0)
        self.write("You lose!", font=("Courier", 24, "normal"))

    def winner_player2(self):
        self.goto(150, 0)
        self.write("You lose!", font=("Courier", 24, "normal"))
        self.goto(x=-250, y=0)
        self.write("You win!", font=("Courier", 24, "normal"))