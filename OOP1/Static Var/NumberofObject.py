class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count +1
    
    @classmethod
    def getNoOfObject(cls):
        print("No of Object", cls.count)
t1=Test()
t2=Test()
Test.getNoOfObject()
t3=Test()
Test.getNoOfObject()
