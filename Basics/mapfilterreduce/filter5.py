def is_Odd(num):
    if num % 2 !=0:
        return True
    else:
        return False
    
l1 = [322,433,5454,3333,5456]
l2 = list(filter(is_Odd, l1))
print(l1)
print(l2)