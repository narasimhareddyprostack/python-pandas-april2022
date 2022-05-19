f = open('abc.txt', 'a+')  #append and read
f.write("Good Morning")
data = f.read()
print(data)
f.close()