import dice_generator
from tkinter import *

def passvalue1():
    var.set(dice_generator.dice1())

def passvalue2():
    var.set(dice_generator.dice1())

gui = Tk()
gui.geometry("300x300")
gui.title("Dice generator")

var = StringVar()

label1 = Label(textvariable = var)
label1.pack()

button1 = Button(gui, text = "Roll dice", command = passvalue1)
button1.pack()

button2 = Button(gui, text = "Roll biased dice", command = passvalue2)
button2.pack() 


gui.mainloop()