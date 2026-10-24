from tkinter import *
screen = Tk()
screen.geometry('500x250')
lable = Label(screen, text='CALLENDER')
lable.pack(side='top')
lable1 = Label(screen, text='Enter Year')
entry = Entry(screen)
lable1.place(x=250, y=125)
screen.mainloop()