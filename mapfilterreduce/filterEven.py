#print first 5 even number - filter
#filter(func, seq)

def even_Num(x):
    if x % 2 ==0:
        return True
    else:
        return False
    
obj = filter(even_Num, range(0,10))
even = list(obj)
print(even)