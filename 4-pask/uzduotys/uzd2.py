def add_functionality(*args):
    """Return sum of provided values"""
    res = 0
    for  x in args:
        res += x
    return res

sum_from_module = add_functionality(8, 2, 3, 0, 7)
print(sum_from_module)

