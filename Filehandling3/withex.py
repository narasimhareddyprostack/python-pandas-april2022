with open('abc.txt', 'r') as f:
    data = f.read()
    print(data)
    print(f.closed)
    

print(f.closed)