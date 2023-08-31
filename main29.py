from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
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


def password_populator():
    password_entry.delete(0, END)
    password = generate_password()
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def empty_field_checker(website, email, password):
    if len(website) == 0 or len(email) ==0 or len(password) ==0:
        messagebox.showinfo(title="Ooops", message="Please, don't leave any fields empty!")
        return False
    else:
        return True


def save():
    """Add the info in the form onto a text file"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if empty_field_checker(website, email, password):
        # messagebox.showinfo(title="Message", message="Message2")
        ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?")

        if ok:
            with open("gabs_manager.txt", mode="a") as file:
                file.write(f"{website:15} | {email:30} | {password}\n")

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
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "gabriela.pinheiro@outlook.com")  # index END end of the sentence

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

### Buttons
generate_button = Button(text="Generate Password", command=password_populator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
