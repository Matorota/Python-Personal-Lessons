#Coffe_maker
class Coffe_maker:

    def __init__(self):
        self.amounts = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.amounts['water']}ml")
        print(f"Milk: {self.amounts['milk']}ml")
        print(f"Coffee: {self.amounts['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.amounts[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make



