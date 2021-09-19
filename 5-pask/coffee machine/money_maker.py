#MoneyMaker
class MoneyMaker:
    def __init__(self, penny, nickel, dime, quarter, half_dollar):
        self.penny = penny
        self.nickel = nickel
        self.dime = dime
        self.quarter = quarter
        self.half_dollar = half_dollar

    def value(self):
        self.penny = 0.01
        self.nickel = 0.05
        self.dime = 0.1
        self.quarter = 0.25
        self.half_dollar = 0.5

    def get_money_info(self):
        """Shows all Money object values"""
        print(input(f"How many pennys:\t\t{self.penny}"))
        print(input(f"How many nickel:\t\t{self.nickel}"))
        print(input(f"How many dime:\t\t{self.dime}"))
        print(input(f"How many quarter:\t\t{self.quarter}"))
        print(input(f"How many half_dollar:\t\t{self.half_dollar}"))
