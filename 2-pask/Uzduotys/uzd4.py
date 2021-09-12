from datetime import datetime

y = int(input("Metai"))
m = int(input("Mon"))
d = int(input("dienos"))

birthday = datetime(y, m, d)

now = datetime.now()
cur = now
ats = birthday - cur
print(ats)
# 4 uzduotis

#input_time = input()
