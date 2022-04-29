l = list(range(20))
print(l)
'''
for ele in l:
    if ele%2 == 0:
        print(ele)
'''
i=0
while i<=len(l)-1:
    if l[i] % 2 ==0:
        print(l[i])
    i=i+1