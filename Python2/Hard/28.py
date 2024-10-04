import pandas as pd

def filter_dataframe(df):
    try:
        filtered_df = df[df['Salary'] > 50000] 
        return filtered_df
    except KeyError as e:
        print(f"KeyError: {e}")

def main():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Salary': [60000, None, 45000, 70000]
    }
    df = pd.DataFrame(data)
    filtered_df = filter_dataframe(df)
    print(filtered_df)
    df['Salary'].fillna(0, inplace=True)
    filtered_df = filter_dataframe(df)
    print(filtered_df)

main()
