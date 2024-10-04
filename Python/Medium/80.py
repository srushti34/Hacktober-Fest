x = 10

def modify_variable():
    x = 5  
    def inner_function():
        global x 
        x += 5  
        print(f"Modified inner x: {x}")

    inner_function()
    print(f"Modified x in outer function: {x}")  

def another_modify_variable():
    x = 20  
    print(f"Another modified x: {x}")  

def main():
    modify_variable()  
    another_modify_variable()  
    print(f"Final x: {x}")  
main()
