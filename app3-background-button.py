from tkinter import *

menu = Tk()

menu.title("Title")
menu.geometry("640x480")
menu['bg'] = 'yellow' # background color

button = Button(menu,text="Run")
button.pack()

menu.mainloop()
