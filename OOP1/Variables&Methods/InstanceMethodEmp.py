class Test:
    def __init__(self):
        self.a=10
    def m1(self):
        print(self.a)
t=Test()
t.m1()
print(t.a)
print(Test.a)