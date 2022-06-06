class Car:
    def __init__(self,name,model,color):
        self.cname=name
        self.cmodel=model
        self.ccolor=color
    def carDetails(self):
        print('Car Name:{}, Model:{}, and Color:{}'.format(self.cname,self.cmodel,self.ccolor))

class User:
    def __init__(self,name,age,car):
        self.name=name
        self.age=age
        self.car=car
    def userDetails(self):
        print('{} has {} car'.format(self.name,self.car.cname))
        self.car.carDetails()
        

c1=Car("Audi", "q7","white")
u=User("Rahul",45,c1)
u.userDetails()