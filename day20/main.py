import time
from turtle import Screen

from day20.score_board import ScoreBoard
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake 🐍")
screen.tracer(0)



my_snake = Snake()

food = Food()

score = ScoreBoard()
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.left,"Left")
screen.onkey(my_snake.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score.increase_score()


    #Detect collision with the wall
    if my_snake.head.xcor() >= 297.5 or my_snake.head.xcor() <= -302.5 or my_snake.head.ycor() >= 302.5 or my_snake.head.ycor() <= -300:
        score.reset()
        my_snake.reset()


    ###Detect collision
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 7.5:
            score.reset()
            my_snake.reset()





screen.exitonclick()
