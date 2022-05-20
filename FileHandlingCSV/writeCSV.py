import csv
f=open("user.csv", 'w')
csvobj = csv.writer(f)
csvobj.writerow(["Eno", "EName","Salary"])
f.close()
