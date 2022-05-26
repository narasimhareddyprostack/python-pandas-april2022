class Employee:
    def __init__(self,id,name,sal):
        self.eid = id
        self.ename=name
        self.esal = sal
    
e1=Employee(101,"Rahul", 45000)
print(e1)
print(e1.__dict__)