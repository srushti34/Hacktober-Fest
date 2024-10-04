import pandas as pd

def merge_dataframes(df1, df2):
    try:
        merged_df = pd.merge(df1, df2, on='ID')
        return merged_df
    except KeyError as e:
        print(f"KeyError: {e}")

def main():
    df1 = pd.DataFrame({
        'ID': [1, 2, 3],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    })
    
    df2 = pd.DataFrame({
        'ID_NUM': [1, 2, 3],
        'Department': ['HR', 'Engineering', 'Sales']
    })
    merged_df = merge_dataframes(df1, df2)
    print(merged_df)
    
    df2.rename(columns={'ID_NUM': 'ID'}, inplace=True)
    merged_df = merge_dataframes(df1, df2)
    print(merged_df)

main()

