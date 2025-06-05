import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.resizemode(rmode="user")
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(0,360))

    def move(self):
        self.forward(30)

    def bounce(self, location):
        if location == "wall":
            self.setheading(self.bounce_math_heading(self.heading(), "horizontal"))
        else:
            self.setheading(self.bounce_math_heading(self.heading(), "vertical"))

    @staticmethod
    def bounce_math_heading(current_heading, orientation):
        if 0 <= current_heading < 90:
            if orientation == "horizontal":
                return 360 - current_heading
            else:
                angle_of_incidence = 90 - current_heading
                return angle_of_incidence + 90
        elif 90 <= current_heading < 180:
            if orientation == "horizontal":
                angle_of_incidence = 90 - (current_heading - 90)
                return angle_of_incidence + 180
            else:
                return 180 - current_heading
        elif 180 <= current_heading < 270:
            if orientation == "horizontal":
                angle_of_incidence = current_heading - 180
                return 180 - angle_of_incidence
            else:
                angle_of_incidence = 270 - current_heading
                return 270 + angle_of_incidence
        else:
            if orientation == "horizontal":
                angle_of_incidence = 360 - current_heading
                return angle_of_incidence
            else:
                angle_of_incidence = current_heading - 270
                return 270 - angle_of_incidence

    def restart(self):
        self.goto(0,0)
        self.setheading(random.randint(0, 360))



