my_mustang = {
    "Brand": "Ford",
    "Model": "Mustang",
    "year": 1969,
    "Good_condition ": True
}

my_nissan = {
    "Brand": "Mercedes benz",
    "Model": "e-klasse",
    "year": 2020,
    "Good_condition " : False
}
my_ziuguliukas = {
    "Brand": "Blinn ",
    "Model": "Blinn 2000",
    "year": 2008,
    "Good_condition " : True
}

print(my_mustang["Brand"])
print(my_mustang.get("Brand"))
print(my_mustang.keys())
print(my_mustang.values())

my_mustang.update({"year" : 2020})
my_mustang["Good_condition"] = False

print(my_mustang)

my_mustang["color"] = (255, 0, 0)
my_mustang["oder cars"] = [my_ziuguliukas, my_nissan]
print(my_mustang)

cars = [my_mustang, my_nissan, my_ziuguliukas]
cars.append(my_ziuguliukas)
print(cars[0]["Model"])
