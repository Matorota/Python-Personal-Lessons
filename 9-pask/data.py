import os
class File:

    # def __init__(self):
    #     self.name = ""

    def read(self):
        file = open("notes.txt", "r")
        print(file.read())
        file.close()

    def update(self): #CHANGE neveikia
        file = open("notes.txt", "r")
        x = input()
        replacement = x
        for line in file:
            line = line.strip()
            line_input = input("to what do you wanna change?")
            line = line_input
            changes = line()
            replacement = replacement + changes + "\n"

        file.close()

        fout = open("notes.txt", "w")
        fout.write(replacement)
        fout.close()

    def add(self):
        with open("notes.txt", "a") as file:
         file.writelines(["\n"])
         file.write(input("\nWhat do you wanna add to your notes?"))
         file.writelines(["\n"])

    def delete(self):  # blogas istrina viska
        with open("notes.txt", "r") as f:
            lines = f.readlines()
        with open("notes.txt", "w") as f:
            for line in lines:
                x = input("Deletes everything(sad)")
                if line.strip("\n") != x:
                    f.write(line)
                else: print("there is no such line")

    def line_counter(self):
        file = open("notes.txt", "r")
        Counter = 0

        # Reading from file
        Content = file.read()
        CoList = Content.split("\n")

        for i in CoList:
            if i:
                Counter += 1

        print("This is the number of lines in the file")
        print(Counter)
        file.close()




