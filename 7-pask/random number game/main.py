# from game_modes import Easy
#
# game_modes = Easy()
#
# is_on = True
#
# while is_on:
#     choice = input(f"Levels:  Easy , Medium , Hard: \n Entr levels name: ")
#
#     if choice == "Easy":
#         game_modes.play()
#     elif choice == "off":
#         is_on = False
#
#     else:
#         print("there is no such level")

from game_modes import Easy
game_modes = Easy()
is_on = True

while is_on:
    choice = input("Write START to play")
    if choice == "off":
        is_on = False
    elif choice == "START":
        game_modes.play()

