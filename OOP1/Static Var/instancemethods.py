#setter and getter
class Bank:
    def setName(self,name):
        self.ename =name
    def getName(self):
        return self.ename
    
c1 = Bank()
c1.setName("Rahul Gandhi")
print(c1.getName())