a = int(input("Enter First Number:"));
b = int(input("Enter Second Number:"));
c = int(input("Enter Third Number:"));
max = a if a>b and a>c else b if b>c else c
print(max)