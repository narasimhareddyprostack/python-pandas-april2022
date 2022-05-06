def fun1():
    a=10      #local var 
    global b  #global
    b=20
    print(a)  #10
    print(b)  #20
    
def fun2():
    #print(a) #NameError
    print(b) #20
fun1()
fun2()