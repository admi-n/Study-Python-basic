#Python #tkinter #button #buttons #GUI #tutorial #beginners #code

from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count+=1
    print(count)

window = Tk()

photo = PhotoImage(file='赞.png')

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="blue",
                activeforeground="#00FF00",
                activebackground="red",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()