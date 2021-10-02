with open("data.txt") as f:
    with open("data2.txt", "w") as f1:
        for line in f:
            f1.write(line)
