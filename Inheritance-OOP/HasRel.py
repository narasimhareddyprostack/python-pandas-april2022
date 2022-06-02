class Mobile:
    def __init__(self,b_Name,m_Name):
        self.brand = b_Name
        self.model =m_Name
    def getMobileDetails(self):
        print('Mobile Brand Name:{} and Model:{}'.format(self.brand, self.model))
class Employee:
    def __init__(self,a,b,c):
        self.id = a
        self.name=b
        self.m = c
    def getEmpDetails(self):
        print("Employee Name:",self.name)
        self.m.getMobileDetails()

m = Mobile("Nokia","c101")
e = Employee(101,"Rahul Gandhi",m)
e.getEmpDetails()