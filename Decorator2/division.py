def  simple_Div(func):
    def inner(a,b):
        if b == 0 :
            print("Cannot divide by Zero")
        else:
            return func(a,b)
    return inner

@simple_Div
def divide(a,b):
    return a/b

print(divide(10,5))  
divide(10,0)

#print(divide(10,0))  # ZeroDivisionError
