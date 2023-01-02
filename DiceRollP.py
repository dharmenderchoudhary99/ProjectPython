from tkinter import *
import random

root = Tk()
root.geometry("700x450")
root.title("Dice Roll")

label=Label(root, text="", font=("times", 260))

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button = Button(root, text="lets roll.....", width = 40, height=5, font=10, bg = "white", bd=2, command = roll)
button.pack(padx=10, pady= 10)


root.mainloop()
