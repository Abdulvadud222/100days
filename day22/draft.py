###classes:
###     player1
###     player2
###     ball
###     scoreboard
###     screen
###     collision with a wall
###     collision with a paddle
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong 🏐")
paddle = Turtle()
paddle.penup()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(5.0, 1.0, 0.0)
paddle.setpos(x=360, y=0)













screen.exitonclick()
















