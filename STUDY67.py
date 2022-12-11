#Python #checkbox #checkbutton #tkinter #GUI #tutorial #beginners

from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar()

python_photo = PhotoImage(file='赞.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='Blue',
                           activeforeground='#00FF00',
                           activebackground='Blue',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')
check_button.pack()


window.mainloop()
