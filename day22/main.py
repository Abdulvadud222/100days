from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong 🏐")
screen.tracer(0)
player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player1.up, "o")
screen.onkey(player1.down, "l")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Updated Paddle Collision Logic
    if ball.distance(player1) < 50 and ball.xcor() > 320:
        if ball.x_move > 0:  # Ensure ball is moving towards the paddle
            ball.bounce_x()

    if ball.distance(player2) < 50 and ball.xcor() < -320:
        if ball.x_move < 0:  # Ensure ball is moving towards the paddle
            ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.player1_point()
        ball.reset_position()


    if ball.xcor() < -400:
        scoreboard.player2_point()
        ball.reset_position()


    if scoreboard.player1_score == 3:
        scoreboard.winner_player2()
        game_is_on = False

    if scoreboard.player2_score == 3:
        scoreboard.winner_player1()
        game_is_on = False










screen.exitonclick()