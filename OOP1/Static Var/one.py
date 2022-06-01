class Bank:
    min_Bal = 500
    def __init__(self,id,name):
        self.id = id
        self.name= name
        
    def open_Acc(self):
        pass
    @classmethod
    def bank_Details(cls):
        cls.bank_Name = "Sbi"
        Bank.city_Name="Bangalore"
        print(cls.min_Bal)
        
c1 = Bank(101,"Rahul")
print(Bank.min_Bal)
Bank.bank_Details()

print(c1.__dict__)
print(Bank.__dict__)
        