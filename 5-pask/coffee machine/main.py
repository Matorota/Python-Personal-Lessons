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


            def caesar_encrypt(realText, step):
                outText = []
                cryptText = []

                uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                for eachLetter in realText:
                    if eachLetter in uppercase:
                        index = uppercase.index(eachLetter)
                        crypting = (index + step) % 26
                        cryptText.append(crypting)
                        newLetter = uppercase[crypting]
                        outText.append(newLetter)
                    elif eachLetter in lowercase:
                        index = lowercase.index(eachLetter)
                        crypting = (index + step) % 26
                        cryptText.append(crypting)
                        newLetter = lowercase[crypting]
                        outText.append(newLetter)
                return outText


            code = caesar_encrypt('abc', 2)
            print()
            print(code)
            print()