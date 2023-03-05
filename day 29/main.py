from tkinter import *
from tkinter import messagebox
import random, pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters_char = [chr(x) for x in range(65, 91)]
    letters_char.extend([chr(x) for x in range(97, 123)])
    numbers_char = [str(x) for x in range(10)]
    symbols_char = [chr(x) for x in range(33,47)]

    password = ""

    for i in range(3):
        password += random.choice(letters_char)
    for i in range(3):
        password += random.choice(symbols_char)
    for i in range(3):
        password += random.choice(numbers_char)

    random.shuffle(list(password))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ups", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail"
        f"\nPassword: {password} \nIs it ok to save?")
        
        #messagebox.showinfo(title="Title", message="Message")
        if is_ok:
            with open("day 29/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=52)
email_entry.insert(0, "test@test.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()