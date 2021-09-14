# po function turi buti 2 tarpai "pass" yra kaip close
def print_soemthing():
    print("Hello world")


def print_something_with_arguments(text):
    print(f"Hello {text}")


def double_number(number):
    result = number * number
    return result


def double_number_with_default_value(number=9):
    return number * number


def more_arguments(make, model, year, color, engine):
    print(f"Make:{make} | model: {model} | yr {year} | color {color} | engine {engine}")


def unknown_arguments(*args):
    print(type(args))
    print(args)


def create_cars(**kvarks):
    # print(type(kvarks))
    # print(kvarks)
    for key, value in kvarks.items():
        print(f"{key.capitalize()}: {value}")


# functuon funcion
def function_outside():
    def funcion_inside():
        print("inside")

    funcion_inside()
    print("outside")


very_important_variable = "very secret password"


def get_very_important_variable():
    global very_important_variable  # global leidzia visur
    very_important_variable = "qqqq"
    print("INSIDE" + very_important_variable)


print_soemthing()
print_something_with_arguments("NKKM")
res = double_number(5)
print(res)
res1 = double_number_with_default_value
print(res1)
# more_arguments("BMW", "5-er", 2020, "red", "petrol")
# more_arguments(model = "BMW", make = "5-er", year = 2020, color = "red", engine = "petrol")
unknown_arguments(566, 46, 456, 4)
create_cars(model="BMW", make="5-er", year=2020, color="red", engine="petrol")
function_outside()
get_very_important_variable()
print("Outside:" + very_important_variable)

