l1 =[10,20,30,40]
def addOne(x):
    return x+1

l2 = list(map(addOne, l1))
print(l1)
print(l2)