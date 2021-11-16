import tkinter as tk
window = tk.Tk()

spin_box = tk.Spinbox(window, from_=10, to=50, increment=1)
spin_box.pack()
window.mainloop()
