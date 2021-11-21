from tkinter import *
from tkinter.ttk import Combobox

com = Tk()


types = StringVar()
elem = ("Strategy", "Action", "Adventure")
box = Combobox(com, value= elem, textvariable = types).pack(pady=20)


com.geometry("250x200")
com.title("ComboBox")
mainloop()
