# importing tkinter module
import tkinter
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

window = Tk()
window.title("10 uzd")
window.minsize(width=500, height=300)


bar = Progressbar(window, length=300, style='black.Horizontal.TProgressbar')
bar['value'] = 80
bar.pack()

window.mainloop()