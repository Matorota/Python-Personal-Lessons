import pandas

data = pandas.read_csv("central_park_squirrels.csv")

grey_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

# print(grey_sq_count)
# print(cinnamon_sq_count)
# print(black_sq_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_sq_count, cinnamon_sq_count, black_sq_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("sq_count.csv")

# Shift
am_sq_shift = len(data[data["Shift"] == "AM"])
pm_sq_shift = len(data[data["Shift"] == "PM"])
# print(am_sq_shift)
# print(pm_sq_shift)

# age
all = len(data["Unique Squirrel ID"])
adult_sq_age = len(data[data["Age"] == "Adult"])
juvenile_sq_age = len(data[data["Age"] == "Juvenile"])
none_sq_age = all - (adult_sq_age+juvenile_sq_age)
print(adult_sq_age)
print(juvenile_sq_age)
print(none_sq_age)




