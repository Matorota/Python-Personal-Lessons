from tkinter import *

window = Tk()
window.minsize(width=500, height=500)

a = "Pirmas tekstas"
b = "Antras tekstas"

text = Text(window)
text.insert(INSERT, a)
text.insert(END, b)
text_to_insert = a + b
text_to_insert = text_to_insert[1:-1]
text.delete(1.0, END)
text.insert(END, text_to_insert)
text.pack()

window.mainloop()
