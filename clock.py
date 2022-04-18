import time
from tkinter import *

root = Tk()

root.geometry("500x200+0+0")

root.configure(background = 'white')
root.resizable(1280,720)

root.overrideredirect(1)

def start():
  text = time.strftime("%I:%M:%S")
  label.config(text=text)
  label.after(200, start)

label = Label(root, font=("Comic Sans MS", 60, 'bold'),  bg = 'white', fg= 'black',bd = 50)
label.grid(row=0, column=1)
start()
print("done")
root.mainloop()

import keyboard

while True:
    if keyboard.read_key() == "p":
        print("You pressed p")
        exit()