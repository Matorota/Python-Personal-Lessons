my_tuple = ("Apple", "Samsung", "Huawei ", "LG", "NO U")

print(type(my_tuple))
print(my_tuple[1])
print(my_tuple[2:4])
print(my_tuple[2])
print(my_tuple[:4])

x = list(my_tuple)
x.append("Dell")
y = tuple(x)
print(y)

unpack = ("Apple", "Samsung",  "Huawei")
(apple, samsung, huawei) = unpack
print((unpack))



