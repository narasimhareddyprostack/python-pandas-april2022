l1 =[10,20,30,40]
'''
def addOne(x):
    return x+1
'''
#l2 = list(map(addOne, l1))
#l2 = list(map(1,2))
#l2 = list(map(fun,seq))
l2 =list(map(lambda x:x+1, l1))
print(l1)
print(l2)