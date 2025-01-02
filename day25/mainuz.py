from turtle import Turtle, Screen

import pandas


turtle = Turtle()
screen = Screen()


screen.title("O'zbekiston viloyatlari!")
image = "uzb_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=1.0, height=1.0)
def state_namer(x_value, y_value, state_name):
    state = Turtle()
    state.penup()
    state.hideturtle()
    state.color("black")
    state.goto(x=x_value, y=y_value)
    state.write(arg=state_name, font=("Arial", 12, "normal"))

name = screen.textinput(title="Foydalanuvchi ma'lumoti", prompt="Ismingizni kiriting:").title()
full_list = pandas.read_csv("uzb_regions.csv")

correct_guesses = 0

game_is_on = True
guesses = []
left_states = []
while game_is_on:

    answer_state = screen.textinput(title=f"{correct_guesses}/13  Viloyatlarni toping",
                                    prompt="Viloyat nomi:").title()


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

    if correct_guesses == 13:
        screen.textinput(title=f"{correct_guesses}/13", prompt="Ajoyib! Siz barcha viloyat va hudud nomlarini topdingiz!")
        game_is_on = False

screen.exitonclick()
