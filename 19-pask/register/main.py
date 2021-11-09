
from csv import DictWriter
from tkinter import *

import pandas
from pandas import *


window = Tk()
window.title("Register")
window.minsize(width=500, height=300)


def button_used():
    if password.get() == re_password.get():
        print("you good")
        csv()
    else:
        print("wrong password")

def csv():
    field_name = ['first name', 'last name', 'username', 'email', 'password']
    input = {'first name':first_name.get(), 'last name':last_name.get(), 'username':username.get(), 'email':email.get(), 'password':password.get()}
    with open('data.csv', 'a') as object:
        dictwrite = DictWriter(object, fieldnames=field_name)
        dictwrite.writerow(input)

    print(object)

label = Label(text="Login", font=("Arial", 14, "bold"))
label.pack()

first_name = Entry(width=30)
first_name.insert(END, string="first name")
first_name.pack()

last_name = Entry(width=30)
last_name.insert(END, string="last name")
last_name.pack()

username = Entry(width=30)
username.insert(END, string="username")
username.pack()

email = Entry(width=30)
email.insert(END, string="email")
email.pack()

password = Entry(width=30)
password.insert(END, string="password")
password.pack()

re_password = Entry(width=30)
re_password.insert(END, string="RePassword")
re_password.pack()

button = Button(text="Submit", command=button_used)
button.pack()


window.mainloop()
