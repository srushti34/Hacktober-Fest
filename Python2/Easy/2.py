try
    file = open('file.txt', 'r')
    content = file.read()
finally
    file.close()
