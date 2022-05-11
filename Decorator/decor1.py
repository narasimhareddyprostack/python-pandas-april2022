def verify(func):
    def inner(name):
        if name == "Modi":
            print("Hello PM,GM")
        else:
            func(name)
            
    return inner

@verify
def employee(name):
    print("Hello",name,",GM")
    
employee("Rahul")
employee("Sonia")
employee("Modi")