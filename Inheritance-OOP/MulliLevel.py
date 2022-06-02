class Parent:
    def m1(self):
        print("Parent Class - m1() method")
    
class Child(Parent):
    def m2(self):
        print("Child Class - m2() method")
    
class GrandChild(Child):
    def m3(self):
        print("Grand child Class - m3() method")

obj = GrandChild()
obj.m1()
obj.m2()
obj.m3()
