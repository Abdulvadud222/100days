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
        self.goto(0, 270)
        self.record = self.load_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.scores}  Record: {self.record}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.scores += 1
        self.update_score()

    def game_over(self):
        if self.scores > self.record:
            self.record = self.scores
            self.save_high_score()
        self.goto(0, 30)
        self.write(f"Record: {self.record}", align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def replay_message(self):
        self.goto(0, -30)
        self.write("Press 'R' to Restart", align=ALIGNMENT, font=FONT)
    @staticmethod
    def load_high_score():
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.record))


