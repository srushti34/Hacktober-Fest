def outer():
    def inner():
        print(x) 
    inner()


x = "5"  


def another_function():
    print("This is another function.")
    inner()  

outer()


def yet_another_function():
    global x
    x = x + 1  

yet_another_function()


print("Final value of x is: " + x) 
