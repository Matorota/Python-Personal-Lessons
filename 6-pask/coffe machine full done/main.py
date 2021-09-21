from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    options = menu.get_items()
  #  dronks = menu.get_drinks()
    choice = input(f"What would you like?({options})")
    #refill_input = input(f"what would you like to refill ({dronks})")

    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    # elif refill_input == "Refill":
    #     print("bruh")
    #     # coffee_maker.refill_macihine()
    #     # Menu.MenuItem()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
