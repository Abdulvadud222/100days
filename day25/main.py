# with open("weather-data.csv") as file:
#     data = file.readlines()



# import csv
#
#
#
# with open("weather-data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures_int_list = []
#     for item in temperatures[1:]:
#         item_int = int(item)
#         temperatures_int_list.append(item_int)
#     print(temperatures_int_list)


# import pandas

# data = pandas.read_csv("weather-data.csv")
# print(type(data))
# print(type(data["temp"]))


# data_dict = data.to_dict()
#
# print(data_dict)



# temp_list = data["temp"].to_list() ### I am getting hold of the column


# print(data["temp"].mean())

#
# max_index = data["temp"].argmax()
#
# max_temp = temp_list[max_index]
# print(max_temp)

# print(data[data.temp == data["temp"].max()])


# monday_row = data[data.day == "Monday"] ### I am getting hold of the row
#
# temp_celsius = int(monday_row.temp)
# temp_fahrenheit = (temp_celsius*1.8) + 32.0
# print(temp_fahrenheit)

# data_dict = {
#     "students": ["Amy", "James", "Angela"], ###Here, students is the column name
#     "scores": [76, 56, 65] ###Here, scores is the column name
# }
#
# data = pandas.DataFrame(data_dict)
#
# print(data)
#
# data.to_csv("new_data.csv")

# full_file = pandas.read_csv("squirrels_data.csv")
#
# file_list = full_file["Primary Fur Color"].to_list()
# gray_count = 0
# cinnamon_count = 0
# black_count = 0
# for item in file_list:
#     if item == "Gray":
#         gray_count += 1
#     elif item == "Cinnamon":
#         cinnamon_count += 1
#     elif item == "Black":
#         black_count += 1
#
# squirrel_count_dict = {
#     "Fur Color": ["grey", "cinnamon", "black",],
#     "Count": [gray_count, cinnamon_count, black_count, ],
# }
#
# squirrel_count_data = pandas.DataFrame(squirrel_count_dict)
#
# squirrel_count_data.to_csv("squirrel_count.csv")



from turtle import Turtle, Screen

import pandas
turtle = Turtle()
screen = Screen()


screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def state_namer(x_value, y_value, state_name):
    state = Turtle()
    state.penup()
    state.hideturtle()
    state.color("black")
    state.goto(x=x_value, y=y_value)
    state.write(arg=state_name, font=("Arial", 8, "normal"))

name = screen.textinput(title="UserName", prompt="What's your name?").title()
full_list = pandas.read_csv("50_states.csv")

correct_guesses = 0

game_is_on = True
guesses = []
left_states = []
while game_is_on:

    answer_state = screen.textinput(title=f"{correct_guesses}/50  Guess the State",
                                    prompt="The name of the State:").title()
    state_row = full_list[full_list.state == answer_state]
    state_row_list = list(full_list.state.to_list())

    if answer_state == "Exit":
        for item in state_row_list:
            if item not in guesses:
                left_states.append(item)
        new_data = pandas.DataFrame(left_states)
        new_data.to_csv(f"States to learn by {name}")
        break


    if answer_state in state_row_list:
        if answer_state not in guesses:
            correct_guesses += 1
        x_cor = int(state_row.x.values[0])
        y_cor = int(state_row.y.values[0])
        state_namer(x_value=x_cor, y_value=y_cor, state_name=answer_state)
        guesses.append(answer_state)

    if correct_guesses == 50:
        screen.textinput(title=f"{correct_guesses}/50", prompt="Good job! You found all the state names!")
        game_is_on = False

screen.exitonclick()




