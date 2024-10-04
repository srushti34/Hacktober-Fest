try:
    file = open('file.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found')
else:
    print('File read successfully')
finally:
    file.close()