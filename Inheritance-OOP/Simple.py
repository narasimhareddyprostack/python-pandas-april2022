class Parent:
    def m1(self):
        print("instance method - Parent")
    @classmethod
    def m2(cls):
        print("class method - Parent")
    @staticmethod
    def m3():
        print("static method - Parent")
        
class Child(Parent):
   def m4(self):
        print("instance method - Child")

c = Child()
c.m1()
c.m2()
c.m3()
c.m4()
