# def print_soemthing(String):
#     print(reversed("Hello world"))
#
#
#
# print(print_soemthing("1234abcd"))


def reverse(String):

    rs = ''
    index = len(String)
    while index > 0:
        rs += String[ index - 1 ]
        index = index - 1
    return rs
print(reverse('1234abcd'))