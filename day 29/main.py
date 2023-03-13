from email import message
from msilib.schema import File
from tkinter import *
from tkinter import messagebox
import random, pyperclip
from turtle import width
import json


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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ups", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail"
        f"\nPassword: {password} \nIs it ok to save?")
        
        #messagebox.showinfo(title="Title", message="Message")
        if is_ok:
            try:
                with open("day 29/data.json", "r") as data_file:
                    #json.load(data_file) #wczyta plik
                    #json.dump(new_data, data_file, indent=4)
                    #data_file.write(f"{website} | {email} | {password}\n")

                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("day 29/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            
            else:
                #Updating old data with new data
                data.update(new_data)

                with open("day 29/data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("day 29/data.json") as data_file:
            data = json.load(data_file)
           
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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
website_entry = Entry(width=31)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=51)
email_entry.insert(0, "test@test.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=31)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()