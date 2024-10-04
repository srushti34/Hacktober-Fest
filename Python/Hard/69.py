x = 10
y = "5"


if x > 5:
    if y > 3: 
        print("y is greater than 3")
    elif x == 10:
        print("x is exactly 10")
    else:
        print("This won't be printed, but it's here anyway")

elif x < 5:
    print("x is less than 5")


else:
    print("x is exactly 5")


if x == "10": 
    print("x is string 10")

if y == 5:  
    print("y is integer 5")

else:
    print("No match for y")
