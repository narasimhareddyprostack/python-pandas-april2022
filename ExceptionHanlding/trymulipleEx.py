try:
    a = int(input("Enter Number:"))
    b = int(input("Enter Number:"))
    print(a/b)
except ValueError as err1:
    print(err1)
except ZeroDivisionError as err2:
    print(err2)