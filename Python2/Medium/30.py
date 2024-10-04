
try:
    file = open('non_existent_file.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found')
    file.close() 
else
    print('File read successfully')  
finally:
    if file:  
        file.close() 
