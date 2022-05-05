emp= {'id':101, 'name':"Rahul", 'Sal':45000}
print(emp.keys())
print(emp.values())
print(emp.items()) #return list of tuples as entry
for k,v in emp.items():
    print(k,":",v)