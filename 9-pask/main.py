from data import File


data = File()

is_on = True

while is_on:
    choice = input(f"Do you wanna add, delete, read notes or update")

    if choice == "add":
        data.add()
    elif choice == "delete":
        data.delete()
    elif choice == "update":
        data.update()
    elif choice == "Read":
        data.read()
    elif choice == "off":
        is_on = False


    else:
        print("there is no such option")
