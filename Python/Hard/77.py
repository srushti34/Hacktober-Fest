import pandas as pd

def resample_time_series(df):
    try:
        resampled = df.resample('M').mean()
        return resampled
    except TypeError as e:
        print(f"TypeError: {e}")

def main():
    data = {
        'Date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01'],
        'Value': [100, 200, None, 400]
    }
    df = pd.DataFrame(data)
    
    try:
        resampled_df = resample_time_series(df)
        print(resampled_df)
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    resampled_df = resample_time_series(df)

    print(resampled_df)

main()
