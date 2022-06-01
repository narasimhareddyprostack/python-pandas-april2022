class Car:
    wheels  = 4         #static variable
    @classmethod
    def drive(cls,cname):
        print('{} has {} wheels'.format(cname,cls.wheels))
    
Car.drive("Dzire")
Car.drive("Innova")

