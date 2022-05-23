try:
    a = int(input("Enter Number:"))
    b = int(input("Enter Number:"))
    print(a/b)

except (ValueError, ZeroDivisionError,NameError) as err:
    print(err)