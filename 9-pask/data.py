import os
class File:

    def __init__(self):
        self.name = ""


    def read(self):
        file = open("notes.txt", "r")
        print(file.read())
        file.close()

    def update(self): #not works
        file = open("notes.txt", "r")
        replacement = self.name()
        for line in file:
            line = line.strip()
            changes = line(input("what kinda what do you wanna change?"))
            replacement = replacement + changes + "\n"

        file.close()

        fout = open("notes.txt", "w")
        fout.write(replacement)
        fout.close()


    def add(self):
        with open("notes.txt", "a") as file:
         file.write(input("What do you wanna add?\n"))
         file.writelines(["\n"])

    f = open("notes.txt", "r")
    print(f.read())
    f.close()

    def delete(self):  # blogas
        with open("notes.txt", "r") as f:
            lines = f.readlines()
        with open("notes.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "name":
                    f.write(line)

    def line_counter(self):
        Counter = 0

        Content = self.read.read()
        CoList = Content.split("\n")

        for i in CoList:
            if i:
                Counter += 1

        print("This is the number of lines in the file")
        print(Counter)



