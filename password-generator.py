import random
from tkinter import *
import string


def password_generator():
    password = []
    for i in range(5):
        ascii_letters = random.choice(string.ascii_letters)
        numbers = random.choice(string.digits)
        symbols = random.choice(string.punctuation)

        password.extend(ascii_letters + numbers + symbols)

        y = "".join(str(x)for x in password)
        lbl.config(text=y)


root = Tk()
root.geometry("250x200")
btn = Button(root, text="Generate Password", command=password_generator)
btn.grid(row=2, column=2)
lbl = Label(root, font=("times", 15, "bold"))
lbl.grid(row=4, column=2)
root.mainloop()
