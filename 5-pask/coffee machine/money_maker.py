#MoneyMaker
class MoneyMaker:
    money = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_got = 0

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.money:
            self.money_got += int(input(f"How many {coin}?: ")) * self.money[coin]
        return self.money_got

    def make_payment(self, price):
        self.process_coins()
        if self.money_got >= price:
            change = round(self.money_got - price, 2)
            print(f"Here is your change{change} .")
            self.profit += price
            return True
        else:
            print("Sorry that's not enough money.")
            return False
        self.money_got = 0
