#Python #tkinter #GUI #tutorial #beginners

from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("860x650")
window.title("My first GUI Program")

icon = PhotoImage(file='杯子.png')
window.iconphoto(True,icon)
window.config(background="black")

window.mainloop() #place window on computer screen, listen for events