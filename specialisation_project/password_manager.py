from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#6527BE"
PURPLE = "#9681EB"
TEAL = "#45CFDD"
MINT = "#A7EDE7"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for item in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    pass_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    pass_numbers = [random.choice(numbers) for n in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password_text.insert(0, password)
    # print(f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_text.get()
    user_id = email_text.get()
    password = password_text.get()
    json_data = {
        website: {
            'user_id': user_id,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(user_id) == 0:
        messagebox.showinfo(title="Error", message="Field can not be empty")

    else:
        with open("password_data.json", 'r') as pass_data:
            # json.dump(json_data, pass_data, indent=4)

            # print(json.load(pass_data))
            data = json.load(pass_data)
            data.update(json_data)

        with open("password_data.json", 'w') as pass_data:
            json.dump(data, pass_data, indent=4)

            # website_text.delete(0, END)
            # password_text.delete(0, END)

#Viewing password#

def view_passwords():
    with open("password_data.json", 'r') as pass_data:
        data = json.load(pass_data)
        passwords = []
        for website, info in data.items():
            passwords.append(f"Website: {website} | User ID: {info['user_id']} | Password: {info['password']}")
        messagebox.showinfo(title="Passwords", message="\n".join(passwords))

#Search passwords #

def search_password():
    website = website_text.get()
    with open("password_data.json", 'r') as pass_data:
        data = json.load(pass_data)
        if website in data:
            info = data[website]
            messagebox.showinfo(title=website, message=f"Website: {website} | User ID: {info['user_id']} | Password: {info['password']}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No password found for {website}")


# UI SETUP
console = Tk()
console.title('Password Manager App Using Tk GUI')
console.config(bg=TEAL)

# Header
header_canvas = Canvas(console, width=320, height=270, bg=MINT, highlightthickness=0)
header_image = PhotoImage(file="logo.png")
header_canvas.create_image(155, 100, image=header_image)
header_canvas.create_text(150, 200, text='Password Manager', fill=PURPLE, font=(FONT_NAME, 18, 'bold'))
header_canvas.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entry Widgets
labels = ['Website:', 'Email/Username:', 'Password:']
for i, label_text in enumerate(labels):
    label = Label(console, text=label_text, bg=TEAL, font=(FONT_NAME, 10))
    label.grid(row=i + 1, column=0, sticky=E, pady=2)
    entry = Entry(console, width=37)
    entry.grid(row=i + 1, column=1, sticky=W, pady=2)
    if i == 1:
        entry.insert(0, 'yawk@gmail.com')  # Default email

# Buttons
add_button = Button(console, text="Add", width=40, command=save_data, bg=PURPLE, fg="black")
add_button.grid(row=4, column=0, columnspan=2, pady=10)

password_generator_button = Button(console, text="Generate Password", command=password_generator)
password_generator_button.grid(row=3, column=1, sticky=E, pady=2)

view_button = Button(console, text="View Passwords", width=40, command=view_passwords, bg=PURPLE, fg="black")
view_button.grid(row=5, column=0, columnspan=2, pady=10)

search_button = Button(console, text="Search Password", width=40, command=search_password, bg=PURPLE, fg="black")
search_button.grid(row=6, column=0, columnspan=2, pady=10)

console.mainloop()
