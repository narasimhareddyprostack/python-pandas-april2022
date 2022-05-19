#print no of lines and no of char and no of words
f = open('abc.txt', 'r')
nl=nc=nw=0
lines = f.readlines()  # read file data into a list 
for line in lines:
    nl = nl + 1
    nc = nc + len(line)
    words = line.split()
    nw = nw + len(words)
    
    
print(nl)
print(nc)
print(nw)
