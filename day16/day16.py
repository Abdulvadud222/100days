# import turtle
# from turtle import Turtle, Screen
#
#
#
# tony = Turtle()
# tony.shape("turtle")
# tony.color("green")
# turtle.dot(20, "red")
# tony.forward(200)
# tony.left(60)
# tony.forward(200)
# tony.left(60)
# tony.forward(200)
# tony.left(60)
# tony.forward(200)
# tony.left(60)
# tony.forward(200)
# tony.left(60)
# tony.forward(200)
# tony.left(60)
# tony.speed(1)
#
# my_screen = Screen()
# var = my_screen.canvheight
# my_screen.exitonclick()



# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander",])
# table.add_column("Type", ["Electric", "Water", "Fire",])
# table.align = "l"
# print(table)
#

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
















