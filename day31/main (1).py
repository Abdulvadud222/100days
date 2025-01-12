from gettext import translation

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

#---------------------------------------------------------Mechanism-----------------------------------------------------------#
def word_chooser():
    import pandas
    import random
    random_index = random.randint(0, 99)
    words = pandas.read_csv("french_words.csv")
    french_words_list = words["French"].to_list()
    english_words_list = words["English"].to_list()
    french_word = french_words_list[random_index]
    english_word = english_words_list[random_index]
    canvas.itemconfig(canvas_image, image=picture)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    def translation():
        canvas.itemconfig(canvas_image, image=next_side)
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=english_word, fill="white")
    if right_button:
        french_words_list.remove(french_word)
        english_words_list.remove(english_word)
    window.after(3000, func=translation)
    if len(french_words_list) == 0:
        breakpoint()





#---------------------------------------------------------UI-----------------------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
picture = PhotoImage(file="card_front.png")
next_side = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=picture)
card_title = canvas.create_text(400, 150, text="Title", font=("Courier", 36, "normal"))
card_word = canvas.create_text(400, 263, text="Word", font=("Courier", 48, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
c_image = PhotoImage(file="right.png")
right_button = Button(image=c_image, highlightthickness=0, command=word_chooser)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column=0, row=1)
w_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=w_image, highlightthickness=0, command=word_chooser)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column=1, row=1)

word_chooser()


window.mainloop()
