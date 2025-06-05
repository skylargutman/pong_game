from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 60, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0,200)
        self.score = [0,0]
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.score[0]} {self.score[1]}",align=ALIGNMENT, font=FONT )

    def update_score(self, side):
        if side == 0:
            self.score[0] += 1
        else:
            self.score[1] += 1
        self.print_score()