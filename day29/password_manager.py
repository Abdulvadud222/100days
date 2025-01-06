from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

#----------------------------------------------Searcher----------------------------------------------------------------#
def searcher():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            stored_website = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Invalid command", message="You have not added your email and password for this website yet!")
    except KeyError:
        if website == "":
            messagebox.showerror(title="Invalid command", message="Please input the name of the website!")
        elif website not in data:
            messagebox.showerror(title="Invalid command", message="You have not added your email and password for this website yet!")
    else:
        stored_email = stored_website["email"]
        stored_password = stored_website["password"]
        messagebox.showinfo(title=f"{website}", message=f"Email: {stored_email}\nPassword: {stored_password}")
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
    window.after(1000, confirmation_label.destroy)

#-----------------------------------------------Saver------------------------------------------------------------------#

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
        "email": email,
        "password": password
        }
    }
    if len(website) ==0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data:
                ###Reading old data
                dic = json.load(data)
                ###Updating old data
                dic.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                ###Saving old data
                json.dump(new_data, data, indent=4)
        else:
            with open("data.json", "w") as data:
                ###Saving old data
                json.dump(dict, data, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            confirmation_label = Label(text="Added!", font=("Courier", 12, "normal"))
            confirmation_label.grid(column=1, row=5, columnspan=2)
            window.after(1000, confirmation_label.destroy)
#-------------------------------------------------UI-------------------------------------------------------------------#
window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)
# Load the image using the corrected path
canvas = Canvas(width=200, height=200)
pic = PhotoImage(file="logo.png")  # Use the dynamically determined path
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
button_search = Button(text="Search", command=searcher)
button_search.config(width=13)
button_search.grid(column=2, row=1)
###Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=38)
# email_entry.insert(END, "@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

window.mainloop()