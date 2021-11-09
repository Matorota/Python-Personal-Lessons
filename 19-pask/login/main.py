from tkinter import *


#  mano nepavykes

# window = Tk()
# window.title("Login")
# window.minsize(width=500, height=300)
# label = Label(text="Login into you account", font=("Arial",14, "bold"))
# label.pack()
#
#
# username_input = Entry(width=15) #
# username_input.pack()
# password_input = Entry(width=15) # priima procentais!
# password_input.pack()
#
# def submit_form():
#     text = username_input.get()
#     text1 = password_input.get()
#     if len(text) > 0: # nebutina
#         name_label = Label(text=text)
#         name_label.pack()
#         name_label1 = Label( text=text1)
#         name_label1.pack()
#
#
# button = Button(text="Submit", command=submit_form)
# button.pack()


# pavykes


from tkinter import *

window = Tk()
window.title("Login")
window.minsize(width=500, height=300)


def button_used():
    print(username_input.get(), password_input.get())


label = Label(text="Login", font=("Arial", 14, "bold"))
label.pack()

username_input = Entry(width=30)
username_input.insert(END, string="Insert your username")
username_input.pack()

password_input = Entry(width=30)
password_input.insert(END, string="Insert your lastname")
password_input.pack()

button = Button(text="Submit", command=button_used)
button.pack()

window.mainloop()

window.mainloop()
