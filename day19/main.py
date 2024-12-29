import random
from turtle import Turtle, Screen
is_race_on = False
screen = Screen()
screen.setup(width = 800, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\n"
                                                          "[blue, red, yellow, pink, orange, green]\nEnter a color: ")
print(user_bet)
ton = Turtle(shape="turtle")
ton.penup()
jon = Turtle(shape="turtle")
jon.penup()
con = Turtle(shape="turtle")
con.penup()
bon = Turtle(shape="turtle")
bon.penup()
ron = Turtle(shape="turtle")
ron.penup()
son = Turtle(shape="turtle")
son.penup()

ton.color("blue")
jon.color("red")
con.color("yellow")
bon.color("pink")
ron.color("orange")
son.color("green")

ton.goto(x=-380, y=-100)
jon.goto(x=-380, y=-50)
con.goto(x=-380, y=0)
bon.goto(x=-380, y=50)
ron.goto(x=-380, y=100)
son.goto(x=-380, y=150)

turtles = [ton, jon, con, bon, ron, son]

def move():
    return random.randint(1,10)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 365:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! The {winning_turtle} turtle is the winner")
            else:
                print(f"You lose! The {winning_turtle} turtle is the winner")
        turtle.forward(move())









# def move_forward():
#     ton.forward(10)
#
# def move_backward():
#     ton.backward(10)
#
# def c_clockwise():
#     ton.left(15)
#
# def clockwise():
#     ton.right(10)
#
# def clear():
#     ton.clear()
#     ton.penup()
#     ton.home()
#     ton.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=c_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)

















screen.exitonclick()