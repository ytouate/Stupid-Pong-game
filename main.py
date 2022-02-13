from turtle import Screen, Turtle
from paddle import *
from ball import *
import time
from scoreboard import *
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
paddle = Paddle(350)
l_paddle = Paddle(-350)

ball = Ball()
screen.listen()
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
scoreboard = ScoreBoard()
game_is_on = True
while game_is_on:
    time.sleep(ball.BallSpeed)
    screen.update()
    ball.move_ball()
    print(ball.BallSpeed)
    # if the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.BallSpeed = 0.1

    # if the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.BallSpeed = 0.1
    # Detect collision with the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 40 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()
        ball.update_speed()


screen.exitonclick()
