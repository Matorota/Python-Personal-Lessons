def group(group_data, no):
    for value in group_data:
        if no == value:
            return True
        return False

print(group([0, 5, 2, 7, 9, 5], 3))
