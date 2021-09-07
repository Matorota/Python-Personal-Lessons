name = "Vardenis"
surname = "Pavardenis"
age = 88

# print("Age" + str(age))
# print(f"Age" + {age})

# quote = f"\tHello my  little friend\n this is my quote \n Author: {name.lower()} {surname.upper()}"
# print(quote)

# paragraph = """"
#    HELLO WORLD
#    THIS IS YOUR
#    MAKER
# """
# print(paragraph)

b_day_wish = """"
Dear {NAME}
Let go of the past; it can't be changed. 
Let go of the future; no one can predict it. 
Also, forget about the present. 
I did not get you one. Happy birthday."""

wishes_for_povilas = b_day_wish.replace("{NAME}", "Povilas")
print(wishes_for_povilas)

