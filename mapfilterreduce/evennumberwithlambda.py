#print(list(filter(lambda  x: x%2 ==0, range(0,10))))
obj = filter(lambda  x: x%2 ==0, range(0,10))
l1 = list(obj)
print(l1)