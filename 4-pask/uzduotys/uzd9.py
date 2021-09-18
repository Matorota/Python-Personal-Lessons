def pr(number):
    if (number==1):
        return False
    elif (number==2): # elif else if
        return True;
    else:
        for x in range(2, number):
            if(number % x==0):
                return False
        return True
print(pr(6))
