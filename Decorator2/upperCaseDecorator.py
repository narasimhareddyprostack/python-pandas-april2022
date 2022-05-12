def to_Upper(func):
    def inner():
        return func().upper()
    return inner  

@to_Upper
def get_Name():
    return "Hello, Rahul!"

print(get_Name())