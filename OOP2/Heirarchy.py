class P:
    def m1(self):
        print("Parent Class - m1 method")
class C1(P):
     def m2(self):
        print("Child 1 Class - m2 method")
class C2(P):
     def m3(self):
        print("Child2 Class - m3 method")
c1=C1()   #Object
c2=C2()   #Object
c1.m1()
c1.m2()
    