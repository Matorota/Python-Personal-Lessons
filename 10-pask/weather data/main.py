import csv
import pandas
from pprint import pprint
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)





with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
   # data_no_header = data[1:]
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)


data = pandas.read_csv("weather_data.csv")
# print(type(data))
data_dict = data.to_dict()
# pprint(data_dict["condition"])
temp_list = data["temp"].to_list()
# print(temp_list)

average_temp = data["temp"].mean() # mean vid
max_temp = data["temp"].max()
min_temp = data["temp"].min()

# print(average_temp)
# print(max_temp)
# print(min_temp)


monday = data[data.day == "Monday"]
# print(monday)
day_with_max_temp = data[data.temp == data.temp.max()]
# print(day_with_max_temp)

monday_temp = int(monday.temp)
monday_condition = monday.condition

print(monday_temp)
print(monday_condition)

data_to_csv = {
    "student": ["01", "02", "03"],
    "grades": [2, 2, 2]
}

data_frame = pandas.DataFrame(data_to_csv)
data_frame.to_csv("students.csv")
print(data_frame)
