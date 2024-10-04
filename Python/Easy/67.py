import pandas as pd

def read_csv(filename)
    try:
        data = pd.read_csv(filename
        return data
    except FileNotFoundError
        print('CSV file not found'

result = read_csv('data.csv'
