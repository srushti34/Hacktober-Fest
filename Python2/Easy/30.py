try:
     result = 10 / 0
except ZeroDivisionError:
     print('Division by zero')
else:
     print('No error')
finally:
     print('Done'