import pandas as pd

def clean():
    df = pd.read_csv("earthquake.csv")
    df1 = df.loc[:,['time', 'latitude', 'longitude', 'depth', 'mag', 'region']].copy()
    df2 =df.loc[:,('place')].str.split(',')
    df1.loc[:,('region')] = df2.str[-1]
    df_clean = df1.dropna().drop_duplicates()

    return df_clean

clean()
