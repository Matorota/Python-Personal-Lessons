# 7 uzduotis
import math

print("(x1, y1) and (x2, y2).")
x = int(input("x = "))
x1 = int(input("x1 = "))
y= int(input("y = "))
y1 = int(input("y1 = "))
p1 = [4, 0]
p2 = [6, 6]

distance = math.sqrt( ((x-x1**2)+((y-y1)**2) ))

distance1= math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)
print(distance1)

