from tkinter import *
import math

root = Tk()
root.title("myapp")
root.geometry("500x400")


def reduce_numbers():
    numirator_3 = int(numirator.get())
    denumirator_3 = int(denumirator.get())
    a = math.gcd(numirator_3, denumirator_3)
    numirator_2.insert(0, numirator_3//a)
    denumirator_2.insert(0,denumirator_3//a)

    


def button_clear():
    numirator.delete(0, END)
    denumirator.delete(0, END)
    numirator_2.delete(0, END)
    denumirator_2.delete(0, END)



#Design
numirator = Entry(root, width=5, borderwidth=5)
numirator.place(x=100, y=20)

denumirator = Entry(root, width=5, borderwidth=5)
denumirator.place(x=100, y=50)
Button_reduce = Button(root, text = "Reduce>>>", command= reduce_numbers)
Button_reduce.place(x=150, y=35)
numirator_2 = Entry(root, width=5, borderwidth=5)
numirator_2.place(x=235, y=20)
denumirator_2 = Entry(root, width=5, borderwidth=5)
denumirator_2.place(x=235, y=50)
Button_clear = Button(root,text = "Clear", command= button_clear)
Button_clear.place(x=300, y=35)


root.mainloop()
