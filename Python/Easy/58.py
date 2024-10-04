def read_lines(filename):
try:
    with open(filename, 'r') as file:
      lines = file.readlines()
except FileNotFoundError:
   print('File not found')
 return lines
result = read_lines('file.txt')