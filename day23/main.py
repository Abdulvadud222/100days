import time
from turtle import Screen


from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

lapse = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    lapse += 1
    if lapse % 5 == 0:
        car_manager.create_cars()
    car_manager.move_cars()
    to_remove = []
    for car in car_manager.cars_list:
        if car.xcor() < -300:
            to_remove.append(car)

    for car in to_remove:
        car_manager.cars_list.remove(car)

    ###if the distance between any car and the turtle is less than 10, the game is over
    for car in car_manager.cars_list:
        if player.distance(car) < 20:
            car_manager.game_over()
            game_is_on = False

    ### if the car reaches the final distance, increase the speed by 5
    if player.ycor() > 280:
        player.reset_the_turtle()
        car_manager.reach += 1
        score_board.level += 1
        score_board.update_level()




screen.exitonclick()