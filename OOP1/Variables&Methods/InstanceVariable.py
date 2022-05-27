class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def m1(self):
        self.c = 30
t1 = Test()
print(t1.__dict__)
t1.m1()
print(t1.__dict__)
