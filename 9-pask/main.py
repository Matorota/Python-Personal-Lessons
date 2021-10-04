from data import File


data = File()

is_on = True

while is_on:
    print("TODO LIST")
    print("you can read line number of thing you have writen down: ReadNum")
    choice = input(f"Do you wanna add line, delete, delete lines, read notes or update:")

    if choice == "add": #veikia
        data.add()
    elif choice == "delete": # viska istrina
        data.delete()
    elif choice == "update": # neveikia
        data.update()
    elif choice == "delete line":
        data.delete_line()
    elif choice == "ReadNum": #veikia
        data.line_counter()
    elif choice == "Read": #veikia
        data.read()
    elif choice == "off":
        is_on = False
    else:
        print("there is no such option")
