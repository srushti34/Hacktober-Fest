def read_csv(filename):
 data = []
 try:
 with open(filename, 'r') as file:
 reader = csv.reader(file)
 for row in reader:
 data.append(row)
 except FileNotFoundError:
 print('CSV file not found')
 return data
result = read_csv('data.csv')