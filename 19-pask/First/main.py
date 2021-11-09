from tkinter import *

window = Tk()
window.title("My first program")
window.minsize(width=500, height=300)

label = Label(text="Your name:", font=("Arial",14, "bold"))
# label1 = Label(text="Your name:", font=("Arial",14, "bold"))

# label.place(height=20, width=130) # pagal x ir y asi

# label.pack() # sujungia viena su kitu
# label1.pack (side=LEFT)

label.grid(column=0, row=0) # cia kaip gridas (excel), turi nuo virsaus prasideti viskas paeiliui
# label1.grid(column=1, row=1, rowspan=2)
#
# label1.config(bg="red") # color

name_input = Entry(width=15) # priima procentais!
name_input.grid(column=0, row=1)


def submit_form():
    text = name_input.get()
    if len(text) > 0: # nebutina
        print("s")
        #1 budas cia neveikia
        # name_label.config(text=text)

        #2 budas
        # name_label = Label(text=text)
        # how i understand used in 1 and 2
        # name_label.grid(column=2, row=3)





button = Button(text="Submit", command=submit_form)
button.grid(column=1, row=2)






window.mainloop()
