huge_list = []

with open("data.txt", "r") as f:
    for line in f:
        huge_list.extend(line.split())
print(huge_list)

