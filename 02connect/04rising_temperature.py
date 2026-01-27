import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.set_index('recordDate')
    df_shifted = df.shift(freq='1D')
    df = pd.merge(left=df, right=df_shifted, how='inner', on='recordDate', suffixes=('_now', '_prev'))
    print(df.head())
    df = df.loc[df['temperature_now'] > df['temperature_prev'], ['id_now']]
    return df.rename(columns={'id_now':'id'})


if __name__ == "__main__":
    data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
    weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})
    print(rising_temperature(weather))