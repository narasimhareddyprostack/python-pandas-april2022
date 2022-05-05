emp= {'id':101, 'name':"Rahul", 'Sal':45000}
print(emp.get('id'))
print(emp.get('loc'))  #if key not available return none
print(emp.get('loc','noida'))

print(emp.keys())
for k in emp.keys():
    print(k)
    
print(emp.values())
for v in emp.values():
    print(v)
    
print(emp.items())