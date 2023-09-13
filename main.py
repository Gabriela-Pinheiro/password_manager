from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generates a random password based on random amount of characters"""
    stock_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    stock_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    stock_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(stock_letters) for _ in range(randint(8, 10))]
    password_list += [choice(stock_numbers) for _ in range(randint(4, 6))]
    password_list += [choice(stock_symbols) for _ in range(randint(4, 6))]

    shuffle(password_list)
    password_generated = "".join(password_list)

    pyperclip.copy(password_generated)
    return password_generated


def populate_password():
    password_entry.delete(0, END)
    password = generate_password()
    password_entry.insert(0, password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    """Look through json file and find 'Website' entry"""
    searched = (website_entry.get()).capitalize()
    try:
        with open("users_manager.json") as file:  # FileNotFound handler
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")

    else:
        if searched in data:
            messagebox.showinfo(title=searched, message=f"Email: {data[searched]['email']}\nPassword: {data[searched]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No {searched.upper()} credential found!\nTry and ADD it instead.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Add the info in the form onto a text file"""
    website = (website_entry.get()).capitalize()
    email = (email_entry.get()).lower()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please, don't leave any fields empty!")
    else:
        try:
            with open("users_manager.json", mode="r") as file:
                data = json.load(file)  # read mode "r"
                data.update(new_data)  # update the file

        except FileNotFoundError:
            with open("users_manager.json", mode="w") as file:
                json.dump(new_data, file, indent=4)  # write mode="w"

        else:
            data.update(new_data)

            with open("users_manager.json", mode="w") as file:
                json.dump(data, file, indent=4)  # write mode="w"

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=220, height=220, padx=100, pady=100)
window.grid()

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

### Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


### Entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "name.surname@outlook.com")  # index END end of the sentence

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

### Buttons
search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=populate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
