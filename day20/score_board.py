from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        with open("data.txt") as file:
            self.highest_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.scores} High Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.scores > self.highest_score:
            self.highest_score = self.scores
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")

        self.scores = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(x=-60, y=0 )
    #     self.write("GAME OVER!", font=FONT)


    def increase_score(self):
        self.scores += 1
        self.clear()
        self.update_score()








