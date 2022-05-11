def outer():
    print("Outer Function")
    def inner():
        print("Inner Function")
    
    return inner

innerfun= outer()
innerfun()
innerfun()
innerfun()
