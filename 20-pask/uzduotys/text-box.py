from tkinter import *

window = Tk()
window.title("Login")
window.minsize(width=500, height=300)


def button_used():
    print(username_input.get(), password_input.get(), code_input.get())


label = Label(text="Login", font=("Arial", 14, "bold"))
label.pack()

username_input = Entry(width=30)
username_input.insert(END, string="Insert your username")
username_input.pack()

code_input = Entry(width=30)
code_input.insert(END, string="Insert your special code")
code_input.pack()

password_input = Entry(width=30)
password_input.insert(END, string="Insert your lastname")
password_input.pack()

button = Button(text="Submit", command=button_used)
button.pack()

window.mainloop()

window.mainloop()
