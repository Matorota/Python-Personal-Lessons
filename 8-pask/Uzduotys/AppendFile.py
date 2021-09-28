with open("data.txt", "a") as file:
    file.write("\nKelintas jau cia kartas?")
    file.writelines(["nzn"])
   # print(file.readlines())

f = open("data.txt", "r")
print(f.read())
f.close()

