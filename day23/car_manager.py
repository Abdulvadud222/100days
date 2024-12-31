COLORS = ["red", "orange", "yellow", "green", "blue", "purple",]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.cars_list = []
        self.reach = 0

    def create_cars(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(1.0, 2.0, 0.0)
        new_car.setheading(180)
        random_color = random.choice(COLORS)
        new_car.color(random_color)
        random_location_y = random.randrange(-250, 251, 30)
        new_car.goto(x=280, y=random_location_y)
        self.cars_list.append(new_car)


    def move_cars(self):
        for car in self.cars_list:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.reach)

    def game_over(self):
        message = Turtle()
        message.penup()
        message.hideturtle()
        message.goto(x=-50, y=0)
        message.write("GAME OVER!", font=("Courier", 24, "normal"))







