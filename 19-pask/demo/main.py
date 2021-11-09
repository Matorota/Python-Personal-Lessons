from tkinter import *

window = Tk()
window.title("Demo")
window.minsize(width=500, height=500)

def button_used():
    print("Button used")

def spinbow_used():
    print(spinbox.get())

def checkbox_used():
    check_state.get()

def radio_used():
    print(radio_state.get())

def listbox_used(event):
    print(list_box.get(list_box.curselection()))

label = Label(text="Label")
label.pack()

button = Button(text="Button", command=button_used)
button.pack()

entry = Entry(width=30)
entry.insert(END, string="Text inserted")
entry.pack()

text = Text(height=5, width=30)
text.pack()

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbow_used)
spinbox.pack()

check_state = IntVar()
check_button = Checkbutton(text="Hello", variable=check_state, command=checkbox_used)
check_button.pack()

radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option-1", value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Option-2", value=2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()

list_box = Listbox(height=4)
colors = ["red", "green", "blue"]

for item in colors:
    list_box.insert(colors.index(item), item)

list_box.bind("<<ListboxSelect>>", listbox_used)
list_box.pack()

window.mainloop()
