n = int(input("Enter No of Employees:"))
emp = {}
i=1
while i<=n:
    ename = input("Enter Employee Name:")
    salary= int(input("Enter Salary:"))
    emp[ename] = salary
    i=i+1
    

print(emp)

for k in emp:
    print(k, ":", emp[k])