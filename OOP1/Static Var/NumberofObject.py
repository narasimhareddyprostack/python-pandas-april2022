class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count +1
    
    @classmethod
    def getNoOfObject(cls):
        print("No of Object", cls.count)
Test()
Test()
Test.getNoOfObject()
Test()
Test.getNoOfObject()
