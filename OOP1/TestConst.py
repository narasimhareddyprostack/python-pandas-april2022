class Test:
    def __init__(self):
        print("Constructor method execute first")
    def m1(self):
        print("method - m1()")
    def m1(self):
        print("method - m1()")
t1=Test()
t2=Test()
t3=Test()
t1.m1()
t2.m1()
t3.m1()