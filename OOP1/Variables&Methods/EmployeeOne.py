class Employee:
    def __init__(self,id):
        self.eid=id
    def setName(self,name):
        self.ename=name
e1 = Employee(101)
#print(e1.__dict__)
e1.setName("Rahul")
e1.sal = 45000
print(e1.__dict__)
print("****")
e2 = Employee(102)
#print(e2.__dict__)
e2.setName("Sonia")
e2.sal = 55000
print(e2.__dict__)