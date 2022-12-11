
#Python #Tkinter #colorchooser #GUI #tutorial #beginners

from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)

    #color = colorchooser.askcolor()
    #window.config(bg=color[1])

    #window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()