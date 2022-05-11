def func():
    print("GM")

a = func    #funciton aliasing
a()
func()
del func
a()
#func()