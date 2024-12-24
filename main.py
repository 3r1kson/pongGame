import time
from turtle import Turtle, Screen

from classes.ball import Ball
from classes.paddle import Paddle
from classes.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
game_on = True

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()
ball = Ball()

def finish_game():
    global game_on
    game_on = False
    screen.bye()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset_position()
        score.score_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.score_r()




screen.exitonclick()