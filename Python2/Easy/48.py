import pandas
def read_csv(filename):
    data = []
    try
         with open(filename, 'r') as file:
             df = pandas.read_csv(file 
             data = df.values.tolist()
    except FileNotFoundError
        print('CSV file not found')
    return data
result = read_csv('data.csv')