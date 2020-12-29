import dice_generator
from tkinter import *
global value
def passvalue1():
    print(dice_generator.dice1())

def passvalue2():
    print(dice_generator.dice2())

gui = Tk()
gui.geometry("300x300")
gui.title("Dice generator")

value = "Roll Dice"

label1 = Label(text = value)
label1.pack()

button1 = Button(gui, text = "Roll dice", command = passvalue1)
button1.pack()

button2 = Button(gui, text = "Roll biased dice", command = passvalue2)
button2.pack()


gui.mainloop()