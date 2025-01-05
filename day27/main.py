from tkinter import * ###we are importing everything


window = Tk()

window.title("Miles to Km")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

###Label
# my_label = Label(text="This is a label", font=("Courier", 24, "italic")) ###this is the alternative of write() in turtle
# # my_label.pack()### the line above won't work unless the code in this line is activated | it has a feature called side(e.g. side="left")
#
# my_label["text"] = "The new label" ### the way of changing the text of the label
# my_label.config(text="The new one") ###another way of changing the text of the label
in_put = Entry(width=5)
# in_put.get() ###this is the way of getting hold of the input(Entry)
# in_put.pack()
in_put.grid(column=1, row=0)
def clicked():
    mile = in_put.get()
    if mile != "":
        km = 1.6 * float(mile)
        label2.config(text=f"{round(km, 1)}")
label = Label(text="Miles", font=("Times New Roman", 12, "normal"))
# label.pack()
# label.place(x=0, y=0)
label.grid(column=2, row=0)

label1 = Label(text="is equal to", font=("Times New Roman", 12, "normal"))
label1.grid(column=0, row=1)
label2 = Label(text="0", font=("Times New Roman", 12, "normal"))
label2.grid(column=1, row=1)
label3 = Label(text="Km", font=("Times New Roman", 12, "normal"))
label3.grid(column=2, row=1)
##Button

button = Button(text="Calculate", command=clicked)
# button.pack()
button.grid(column=1, row=2)



###Entry
































# ###labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# ###buttons
# def action():
#     print("Do something")
#
# ###call action() when pressed
#
# button = Button(text="Click me", command=action)
# button.pack()
#
# ###entries
# entry = Entry(width=30)
# ###Add some starting text to begin with
# entry.insert(END, string="Some Text To Begin With.")
# ###Get the text in the entry
# message = entry.get()
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #put cursor in textbox
# text.focus()
# ###Add some starting text to begin with
# text.insert(END,"Write something")
# #get current value in textbox at line 1 character 0
# text_message = text.get("1.0", END)
# text.pack()
# ###Spinbox
# def spinbox_used():
#     print("Spinbox used")
# spinbox = Spinbox(from_=0, to=10, width=5, command="")
# spinbox.pack()
#
# ###Scale
# ###Called with current scale value
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
# ###Check button - Several options can be selected
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="is On?", variable = checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# ###Radiobutton only
# def radio_used():
#
#     print(radio_state.get())
# #variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable = radio_state, command=radio_used)
# radio_state = IntVar()
# radiobutton2 = Radiobutton(text="Option2", value=2, variable = radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# ###Listbox
# def listbox_used(event):
#     #Gets current selection from the box
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
#
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


window.mainloop()
