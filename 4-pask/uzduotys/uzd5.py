def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
number=int(input("Input a number to compute the factiorial : "))
print(factorial(number))


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))