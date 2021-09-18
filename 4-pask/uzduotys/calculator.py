print("Skaicuotuvas.")
print("apskaiciavimas")
print("1.Prideti")
print("2.minusuoti")
print("3.dauginti")
print("4.padalinti")

def add(x, y):
   return x + y


def subtract(x, y):
   return x - y


def multiply(x, y):
   return x * y


def divide(x, y):
   return x / y

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Numeris 1: "))
num2 = int(input("Numeris 2: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("no")