class Test:
    def __init__(self):
        self.a=10

t1 = Test()
del t1.a
t2 = Test()
print(t1.__dict__)
print(t2.__dict__)