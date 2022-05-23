a = int(input("Enter Number:"))
b = int(input("Enter Number:"))
try:
    print(a/b)
except ZeroDivisionError:
    print(a/1)