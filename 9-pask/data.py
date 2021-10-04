import os
import re

class File:
    def read(self):
        file = open("notes.txt", "r")
        print(file.read())
        file.close()

    def update(self): #CHANGE neveikia
        with open("notes.txt", "r+") as file:
            text =file.read()
            wrtie_word = str(input("What to replace?"))
            replace_word = str(input("replace to:"))
            text = re.sub(wrtie_word,replace_word,text)
            file.seek(0)
            file.write(text)
            file.truncate()


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
                else: print("there is no ESCAPE")

    def delete_line(self):
        lineSkip = int(input("Line number:"))
        with open("notes.txt", "r") as fp:
            lines = fp.readlines()
        current_line = 1
        with open("notes.txt", "w") as wf:
            for line in lines:
                if current_line == lineSkip:
                    pass
                else:
                    wf.write(line)
                current_line += 1

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




