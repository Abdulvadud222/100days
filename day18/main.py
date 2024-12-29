# import turtle as t ###this is used to shorten the name of the module. Now I don't have to use the full word turtle, instead I can use t

# import heroes
# import villains

# def create_angle():
#     ton.forward(120)
#     ton.right(90)
#     ton.forward(60)
#     ton.right(90)
# create_angle()
# create_angle()


# def create_square():
#     ton.forward(100)
#     ton.right(90)
# for i in range(4):
#     create_square()

# def line():
#     ton.forward(10)
# def blank():
#     ton.penup()
#     ton.forward(10)
#     ton.pendown()
#
#
# for i in range(15):
#     line()
#     blank()

from turtle import Turtle, Screen
ton = Turtle()
screen = Screen()
screen.colormode(255)
ton.shape("arrow")
ton.color("PaleTurquoise2")
ton.pensize(0)
ton.speed(0)
# def random_color():
#     import random
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     return ton.fillcolor(red, green, blue), ton.pencolor((red, green, blue))
# ###drawing a shape
# n = 3
# for times in range(7):
#     random_color()
#     for i in range(n):
#         ton.forward(50)
#         ton.right(360/n)
#     n += 1




####Drawing a random walk

# for i in range(200):
#     import random
#     random_color()
#     direction = random.randint(1, 4)
#     if direction == 1:
#         ton.forward(30)
#     elif direction == 2:
#         ton.back(30)
#     elif direction == 3:
#         ton.right(90)
#         ton.forward(30)
#     elif direction == 4:
#         ton.left(90)
#         ton.forward(30)
# for i in range(36):
#     random_color()
#     ton.circle(100)
#     ton.right(10)

### the one that starts from home
# import colorgram
#
# colors = colorgram.extract('image.jpg', 225)
# colors_list = []
# for color in colors:
#     rgb = color.rgb
#     colors_list.append((rgb.r, rgb.g, rgb.b))
# colors_list = colors_list[4:]
# v = 0
# h = 0
# for i in range(15):
#     for _ in range(15):
#         ton.dot(10, colors_list[h % len(colors_list)])
#         ton.penup()
#         ton.forward(20)
#         h += 1
#     ton.home()
#     ton.left(90)
#     ton.forward(20 + v*20)
#     ton.right(90)
#     v += 1



### the one that starts from a lower position
# import colorgram
#
# colors = colorgram.extract('image.jpg', 225)
# colors_list = []
# for color in colors:
#     rgb = color.rgb
#     colors_list.append((rgb.r, rgb.g, rgb.b))
# colors_list = colors_list[4:]
# v = 0
# h = 0
# ton.penup()
# ton.goto(-100, -120 + v * 20)
# for i in range(15):
#     for _ in range(15):
#         ton.dot(10, colors_list[h % len(colors_list)])
#         ton.penup()
#         ton.forward(20)
#         h += 1
#     ton.penup()
#     ton.goto(-100, -100 + v * 20)  # Move the turtle down by 20 * v each row
#     v += 1


screen.exitonclick()