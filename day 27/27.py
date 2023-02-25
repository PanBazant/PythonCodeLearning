import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(800,800)
window.config(padx=200, pady=200) # dodanie paddingu do obiektu


#Label
my_label = tkinter.Label(text="Label", font=("Arial", 24))
my_label.grid(column=0, row=0) # umieszcza na screenie

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)
#Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


#pack() ustawia widgety po kolei z góry na dół
#pack(side="left") zacznie umieszczać elementy od lewej strony
# problemem z pack() jest precyzja umieszaczania elementów

#place(x=0, y0) - podajemy parametry określające odległość od lewego górnego rogu okna


#grid(column=0, row=0) relatywny system pozycjonowania
# nie można mieszać grid() i pack()

window.mainloop()