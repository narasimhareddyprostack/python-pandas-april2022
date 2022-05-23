try:
    f= open("abc.txt")
    data= f.read()
    print(data)
    f.close()
    
except FileNotFoundError as err:
    f=open('abc.txt')
    data=f.read()
    print(data)
    
