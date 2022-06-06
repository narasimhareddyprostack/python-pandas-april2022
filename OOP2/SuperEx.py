class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def userDetails(self):
        print('Name:{}, and Age:{}'.format(self.name,self.age))

class Employee(User):
    def __init__(self,id,name,age,sal,city):
        super().__init__(name,age)
        self.eid=id
        self.esal=sal
        self.city=city
    def empDetails(self):
        super().userDetails()

e1=Employee(101,"Rahul",45,45000,"New Delhi")
e1.empDetails()