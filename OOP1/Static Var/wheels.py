class Car:
    wheels  = 4         #static variable
    def __init__(self):
        pass
    def service(self):
        pass
    @classmethod
    def drive(cls,cname):
        print('{} has {} wheels'.format(cname,cls.wheels))
    @staticmethod
    def m1():
        pass
    
Car.drive("Dzire")
Car.drive("Innova")

