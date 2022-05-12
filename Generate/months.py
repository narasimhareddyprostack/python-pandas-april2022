a = 10
print(type(a))

def gen_Months():
    print("generating Months")
    yield "JAN"
    yield "FEB"
    yield "MAR"
    yield "APR"
    
    
g = gen_Months()
print(type(g))
for x in g:
    print(x)