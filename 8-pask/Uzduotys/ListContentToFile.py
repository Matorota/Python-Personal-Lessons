color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('data.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('data.txt')
print(content.read())
# paraso daiktus bet istrina buvisius