try:
    a = int(input("Enter Number:"))
    b = int(input("Enter Number:"))
    print(a/b)
    print("GM")

except ZeroDivisionError as err:
    print(err)