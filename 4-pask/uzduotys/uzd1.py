#internet version
# def print_max(a, b, c):
#     if (a >= b) and (a >= c):
#         max = a
#     elif (b >= a) and (b >= c):
#         max = b
#     else:
#         max = c
#
#     return max
#
#     a = 10
#     b = 14
#     c = 12
#     print(print_max(a, b, c))

#simple
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)



a = 10
b = 14
c = 12
print(maximum(a, b, c))