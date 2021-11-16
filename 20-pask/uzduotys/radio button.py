import tkinter as T
window = T.Tk()
window.title("Radiobutton ")
window.geometry('350x200')
radio1 = T.Radiobutton(window, text='First', value=1)
radio2 = T.Radiobutton(window, text='Second', value=2)
radio3 = T.Radiobutton(window, text='Third', value=3)
radio1.grid(column=0, row=0)
radio2.grid(column=1, row=0)
radio3.grid(column=2, row=0)

window.mainloop()

