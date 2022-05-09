#filter(function, sequence)

l1 = [3,4,5,6]

x = filter(lambda num: num % 2 == 0,l1)
l2= list(x)
print(l1)
print(l2)
print(list(filter(lambda x : x % 2 ==0 ,[3,4,5,6]) ))
