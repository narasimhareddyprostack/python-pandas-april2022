#WAP to print first 10 even number
#print(list(filter(lambda x:x %2 ==0, range(0,19))))
def is_Even(x):
    if x % 2 ==0:
        return True
    else:
        return False
    
l1 = list(range(0,19))
print(l1)
l2 = list(filter(lambda x:x %2 ==0, l1))
print(l2)

        