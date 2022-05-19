f = open("abc.txt", 'r')
data =f.read()  # to read entire file data
data1 = f.read(10)  # To read n no of char
print(data1)
f.close()