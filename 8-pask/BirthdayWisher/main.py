import  os
PLACEHOLDER = "[name]"


def check_if_names_exists():
    if os.path.exists("./names") and os.path.exists("./names/names.txt"):
        print("names  found")
        return True
    else:
        print("names not found")
        return False


def check_if_wish_exists():
    if os.path.exists("./wish") and os.path.exists("./wish/wish.txt"):
        print("wish found")
        return True

    else:
        print("wish not found")
        return False


with open("./names/names.txt") as name_file:
    names = name_file.readlines()
    print(names)

with open("./wish/wish.txt") as wish_file:
    wish = wish_file.read()

    if not os.path.exists("output"):
        print("Folder not Found, creating bew one...")
        os.mkdir("output")

    print("Generating")

    for name in names:
        stripped_name = name.strip()
        new_wish = wish.replace(PLACEHOLDER, stripped_name)
        print(new_wish)

        with open(f"./output/b-day-wish{stripped_name.lower()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_wish)
