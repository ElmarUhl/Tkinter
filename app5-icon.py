from tkinter import *

menu_initial = Tk()
menu_initial.title("First App")

menu_initial.geometry("500x250+200+200")
menu_initial.resizable(True,True)

#menu_initial.state("zoomed")
#menu_initial.state("iconic")
menu_initial.iconbitmap(bitmap="images/whatsapp.ico")

menu_initial.mainloop()
