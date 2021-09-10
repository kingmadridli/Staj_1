from tkinter import *
import time
from random import randint
import threading



root = Tk()

root.title("Threading")
root.geometry("500x400")

def FiveSeconds():
    time.sleep(5)
    my_label.config(text="5 sec is up!")


def RandomNumber():
    random_label.config(text=f"Random number is {randint(1,100)}")



my_label = Label(root,text="Hello There")
my_label.pack(pady=20)

my_button1 = Button(root,text="5 seconds",command=threading.Thread(target=FiveSeconds).start())
my_button1.pack(pady=20)

my_button2 = Button(root,text="pick random number",command=RandomNumber)
my_button2.pack(pady=20)

random_label = Label(root,text="")
random_label.pack(pady=20)

root.mainloop()