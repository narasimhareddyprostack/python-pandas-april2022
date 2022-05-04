x = [10,20,30]
y = x.copy()
x[0] = 100
print(x)
print(y)
print(id(x))
print(id(y))

