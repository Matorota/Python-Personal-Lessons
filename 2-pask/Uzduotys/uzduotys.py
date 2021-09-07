from datetime import datetime, date

# 1 uzduotis

first_ex = """
Twinkle, twinkle, little star
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are
"""

print(first_ex)

# 2 uzduotis

name_str = input("enter your name:")
surname = input("enter your surname:")

print(f"name: {name_str}\n surname:{surname}")

# 3 uzduotis

past_date = datetime(2020, 5, 6)
today_date = datetime.now()
atsakymukas = today_date - past_date
print(atsakymukas.days)

# 4 uzduotis

#input_time = input()

# 5 uzduotis

h = int(input("h = "))
b = int(input("b = "))
answer = h * b / 2
print(f"5Answer: {answer}")

# 6 uzduotis

print("(x + y) * (x + y).")
x = int(input("x = "))
y = int(input("y = "))
ats = (x + y) * (x + y)
print(f"6Answer: {ats}")

# 7 uzduotis


