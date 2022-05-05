emp= {'id':101, 'name':"Rahul", 'Sal':45000}

removed_Value  = emp.pop('Sal')
print(emp)
print(removed_Value)

emp.popitem()
print(emp)
emp.clear()
print(emp)