def dublication_def(*args):
    """Return dublicate all provided values"""
    res = 1
    for  x in args:
        res = res * x
    return res

duplicate = dublication_def(8, 2, 3, -1, 7)
print(duplicate)