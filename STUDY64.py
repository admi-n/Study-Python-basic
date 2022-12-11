from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()
window.title("A laber")
photo = PhotoImage(file=r'C:\Users\琚晨阳\Pictures\aaaa.png')

label = Label(window,
              text="HELLO,WORLD",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=40,
              padx=40,
              pady=40,
              image=photo,
              compound='bottom')
label.pack()
#label.place(x=0,y=0)

window.mainloop()
