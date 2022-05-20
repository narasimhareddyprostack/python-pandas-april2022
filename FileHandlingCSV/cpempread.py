import csv
f = open('cpemp.csv','r')
data = csv.reader(f)  #return csv object
print(data)
#print(list(data))
for line in list(data):
    for x in line:
        print(x, "\t",end="")
    print()