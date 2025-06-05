import time
from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

def draw_line():
    # draw line down middle
    t = Turtle()
    t.penup()
    t.ht()
    t.color("white")
    t.width(5)
    t.goto(0, -300)
    t.setheading(90)
    for _ in range(0, 30):
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong! The game!")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
scoreboard.print_score()

left_paddle = Paddle("left")
right_paddle = Paddle("right")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

draw_line()

ball = Ball()

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    ball.move()

    #detect ball hitting top or bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce("wall")

    #detech ball hitting a paddle
    if ball.distance(left_paddle) < 45 or ball.distance(right_paddle) < 45:
        ball.bounce("paddle")

    #detect ball hitting left or right sides
    if ball.xcor() > 380:
        scoreboard.update_score(0)
        ball.restart()
    elif ball.xcor() < -380:
        scoreboard.update_score(1)
        ball.restart()


screen.exitonclick()