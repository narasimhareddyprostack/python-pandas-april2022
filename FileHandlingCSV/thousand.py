import csv
f = open('1000.csv')
data= list(csv.reader(f))
for line in data:
    for x in line:
        print(x,"\t", end="")
    print()
f.close()
