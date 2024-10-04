import pandas as pd

def concatenate_dataframes(df1, df2):
    try:
        concatenated = pd.concat([df1, df2], axis=1) 
        return concatenated
    except ValueError as e:
        print(f"ValueError: {e}")

def main():
    df1 = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    
    df2 = pd.DataFrame({
        'C': [7, 8],
        'D': [9, 10]
    })
    
    
    concatenated_df = concatenate_dataframes(df1, df2)
    print(concatenated_df)
    
   
    df2 = df2.reindex(index=df1.index)
    concatenated_df = concatenate_dataframes(df1, df2)
    print(concatenated_df)

main()
