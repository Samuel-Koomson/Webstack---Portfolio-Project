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

# UI SETUP #

console = Tk()
console.title('Password Manager App Using Tk GUI')
console.config(width=500, height=500, padx=80, pady=50, bg=TEAL)

console_canvas = Canvas(width=300, height=300, bg=MINT, highlightthickness=0)
canvas_image = PhotoImage(file="logo.png")
console_canvas.create_image(145, 150, image=canvas_image)
console_canvas.create_text(150, 50, text='Password Manager',  fill=PURPLE, font=(FONT_NAME, 18, 'bold'))
console_canvas.place(x=20, y=-15)

website_label = Label(text='Website:')
website_label.place(x=20, y=305)

email_label = Label(text='Email/Username:')
email_label.place(x=0, y=320)

password_label = Label(text='Password:')
password_label.place(x=20, y=336)

website_text = Entry(width=37)
website_text.place(x=100, y=300)
website_text.focus()

email_text = Entry(width=37)
email_text.place(x=100, y=320)
email_text.insert(0, 'yawk@gmail.com')

password_text = Entry(width=18)
password_text.place(x=100, y=340)

add_button = Button(text="Add", width=25, command=save_data)
add_button.place(x=100, y=365)

password_generator_button = Button(text="Generate Password", command=password_generator)
password_generator_button.place(x=215, y=340)
password_generator_button.config(padx=0, pady=0)

view_button = Button(text="View Passwords", width=25, command=view_passwords)
view_button.place(x=100, y=395)

search_button = Button(text="Search Password", width=25, command=search_password)
search_button.place(x=215, y=395)

console.mainloop()
