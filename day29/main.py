from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
#-----------------------------------------Password Generator-----------------------------------------------------------#
def password_generator():
    letter_length = random.randint(8, 10)
    symbol_length = random.randint(2, 4)
    number_length = random.randint(2, 4)

    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    numbers = ["0", "1", "2", "3", "4", "5", "6," "7", "8", "9"]

    rand_letters = random.choices(letters, k = letter_length) ###now I get letter_length times random letters from letters by using this "k ="
    rand_symbols = random.choices(symbols, k = symbol_length)
    rand_numbers = random.choices(numbers, k = number_length)

    password_list = rand_letters + rand_symbols + rand_numbers ###this puts all three lists into one list

    random.shuffle(password_list) ###this shuffles the list
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    confirmation_label = Label(text="Copied to clipboard", font=("Courier", 12, "normal"))
    confirmation_label.grid(column=1, row=5, columnspan=2)
    window.after(2000, confirmation_label.destroy)

#-----------------------------------------------Saver------------------------------------------------------------------#

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) ==0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The details entered:\nWebsite: {website}\nEmail: {email}\n"
                               f"Password: {password}\nDo you want to add these details?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                confirmation_label = Label(text="Added!", font=("Courier", 12, "normal"))
                confirmation_label.grid(column=1, row=5, columnspan=2)
                window.after(1000, confirmation_label.destroy)
        else:
            confirmation_label = Label(text="Not added!", font=("Courier", 12, "normal"))
            confirmation_label.grid(column=1, row=5, columnspan=2)
            window.after(1000, confirmation_label.destroy)

#-------------------------------------------------UI-------------------------------------------------------------------#
window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)
canvas = Canvas(width=200, height=200)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)
###Labels
label_website = Label(text="Website:", font=("Courier", 12, "normal"))
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:", font=("Courier", 12, "normal"))
label_email.grid(column=0, row=2)
label_password = Label(text="Password:", font=("Courier", 12, "normal"))
label_password.grid(column=0, row=3)
space_for_added = Label(text="", font=("Courier", 12, "normal"))
space_for_added.grid(column=1, row=5, columnspan=2)
###Button
button_generate_password = Button(text="Generate Password", command=password_generator)
button_generate_password.grid(column=2, row=3)
button_add = Button(text="Add", command=save)
button_add.config(width=36)
button_add.grid(column=1, row=4, columnspan=2)
###Entries
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
# email_entry.insert(END, "@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

window.mainloop()