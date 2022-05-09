#WAP to print factorial of given number
def fact(n):
    i = 1
    while n >=1:
        i = i*n
        n = n -1
    return i


result = fact(5)
print(result)