class GetMarrySoon(Exception):
    def __init__(self,arg):
        self.msg = arg

age = int(input("Enter Your age:"))
try:
    if age>24:
        print("Eligible for Marriage")
    else:
        raise GetMarrySoon("Not Eligible")
except GetMarrySoon as xyz:
    print(xyz)
print("Hello,GM")