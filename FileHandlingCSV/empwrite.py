import csv
f=open("cpemp.csv", 'w',newline="")

csvobj = csv.writer(f)

csvobj.writerow(["Eno", "EName","Salary"])
n = int(input("Enter no of Employees:"))
for  x in range(n):
    eno =  int(input("Enter Employee No:"))
    ename= input("Enter Employee Name:")
    esal=  int(input("Enter Salary:"))
    csvobj.writerow([eno,ename,esal])
    
f.close()
