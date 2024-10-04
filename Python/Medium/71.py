try:
    result = 10  
except ZeroDivisionError:
    print('Division by zero')
else:
    print('No error, but there was no division either!')  
finally:
    print('Done')
