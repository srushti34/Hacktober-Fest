def outer():
     x == 10
def x():
         global x  # Error: x is local to outer and cannot be made global
         x=5
         x()
        
outer()
print(x)
