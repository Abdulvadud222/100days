import time
from turtle import Screen

from score_board import ScoreBoard
from snake import Snake
from food import Food

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake 🐍")
screen.tracer(0)

# Global variables
my_snake = Snake()
food = Food()
score = ScoreBoard()


def start_game():
    global my_snake, food, score

    # Clear previous game state
    screen.clear()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("The Snake 🐍")
    screen.tracer(0)

    # Initialize game objects
    my_snake = Snake()
    food = Food()
    score = ScoreBoard()

    # Key bindings
    screen.listen()
    screen.onkey(my_snake.up, "Up")
    screen.onkey(my_snake.down, "Down")
    screen.onkey(my_snake.left, "Left")
    screen.onkey(my_snake.right, "Right")

    game_loop()


def game_loop():
    global my_snake, food, score

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(max(0.05, 0.1 - score.scores * 0.005))
        my_snake.move()

        # Detect collision with food
        if my_snake.head.distance(food) < 15:
            food.refresh()
            my_snake.extend()
            score.increase_score()

        # Detect collision with walls
        if (
            my_snake.head.xcor() >= 297.5
            or my_snake.head.xcor() <= -302.5
            or my_snake.head.ycor() >= 302.5
            or my_snake.head.ycor() <= -300
        ):
            game_is_on = False
            score.game_over()
            score.replay_message()

        # Detect collision with tail
        for segment in my_snake.segments[1:]:
            if my_snake.head.distance(segment) < 7.5:
                game_is_on = False
                score.game_over()
                score.replay_message()
    screen.onkey(start_game, "r")


# Start the game and bind restart key
start_game()

screen.exitonclick()
