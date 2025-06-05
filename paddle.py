from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.resizemode(rmode="user")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.color("white")
        if side == "right":
            self.goto(350, 0)
        else:
            self.goto(-350,0)

    def up(self):
        self.forward(60)

    def down(self):
        self.backward(60)