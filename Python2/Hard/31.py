import pandas as pd

def create_pivot_table(df):
    try:
        pivot = pd.pivot_table(df, values='Sales', index='Product', columns='Region', aggfunc='sum')
        return pivot
    except KeyError as e:
        print(f"KeyError: {e}")

def main():
    data = {
        'Product': ['A', 'B', 'A', 'C', 'D', None],
        'Region': ['East', 'West', 'North', 'South', None, 'East'],
        'Sales': [100, 200, 150, None, 300, 250]
    }
    df = pd.DataFrame(data)
   
    pivot_table = create_pivot_table(df)
    print(pivot_table)
    
   
    try:
        pivot_table = pd.pivot_table(df, values='NonExistentColumn', index='Product', columns='Region', aggfunc='sum')
    except KeyError as e:
        print(f"KeyError: {e}")

main()

