from money_maker import MoneyMaker
from menu import Menu, MenuItem
from coffee_maker import Coffe_maker
from money_maker import MoneyMaker

menu = Menu()
name = menu.get_items()
money_machine = MoneyMaker()
coffee_maker = Coffe_maker()
w_continue = True
while w_continue:
    choice = input(f"What would you like? ({name}): ")
    if choice == "report":
        w_continue = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker



