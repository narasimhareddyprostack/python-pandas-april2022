def cal(*n):
    sum=0
    #print(n)
    for x in n:
        sum =sum+x
    
    print(sum)
    

cal(10,20,30)    # 60
cal(1,2)         # 3
cal(1,2,3,4,5,6,7,8,9) #45