class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def change_human(self, name, age, height):
        """change human inside object"""
        self.name = name
        self.age = age
        self.height = height


    def get_human_info(self):
        """Shows all Human object values"""
        print(f"Name:\t\t{self.name}")
        print(f"age:\t\t{self.age}")
        print(f"height:\t\t{self.height}")


