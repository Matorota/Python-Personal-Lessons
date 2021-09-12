germna_cars = ["BMW", "AUDI", "Porsche", "Cat", "Blitz", "bruh"]

for car in germna_cars:
    print(car)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in germna_cars[:2]:
    print(x)

for x in range(5, 100, 5):
    print(x)

my_mustang = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "year" : 1969,
    "Good_condition " : True
}

for key, value in my_mustang.items():
    print(f"keys:{key}  value: {value}")

