from tkinter import *



def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        from tkinter.messagebox import showwarning
        showwarning("Wrong")


def deleteTask():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('800x450+800+200')
ws.title('To_Do')
ws.resizable(width=False, height=False)


issues = Label(text= "Issues")
issues.pack(side=LEFT)

done_issues = Label(text= "Done Issues")
done_issues.pack(side=RIGHT)

ongoings = Label(text= "Ongoing")
ongoings.pack()
frame = Frame(ws)
frame.pack(pady=4 )



lb = Listbox(
    frame,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,

)
done_lb = Listbox(
    frame,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,

)
ongoing = Listbox(
    frame,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,

)
lb.pack(side=LEFT)
done_lb.pack(side=RIGHT)

task_list = []

for item in task_list:
    lb.insert(END, item)

# sb, lb
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

sbs = Scrollbar(frame)
sbs.pack(side=RIGHT, fill=BOTH)

done_lb.config(yscrollcommand=sbs.set)
sbs.config(command=done_lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add',
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame, text='Delete ',command=deleteTask )
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
