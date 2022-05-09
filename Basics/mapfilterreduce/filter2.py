def is_Even(num):
    if num % 2 == 0:
        return True
    else:
        return False
l1 = [10,4,3,6,7,8]

l2 = list(filter(is_Even,l1))
print(l1)
print(l2)

