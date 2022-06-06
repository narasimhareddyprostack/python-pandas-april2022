class F:
    def m1(self):
        print("Father Class - m1 Method")
class M:
    def m1(self):
        print("Mother Class - m1 Method")
        
class C(M,F):
    def m2(self):
        print("Child Class - m2 Method")
c = C()
c.m1()
c.m2()
