import pandas as pd

def clean():
    df = pd.read_csv("earthquake.csv")
    df1 = df.loc[:,['time', 'latitude', 'longitude', 'depth', 'mag', 'region']].copy()
    df2 =df.loc[:,('place')].str.split(',')
    df1.loc[:,('region')] = df2.str[-1]
    df_clean = df1.dropna().drop_duplicates()

    return df_clean

def mag_region():
    df_clean = clean()
    df_clean.mag = pd.cut(df_clean.mag, bins=[0, 2, 5, 7, 9, 10], labels=['micro', 'light', 'strong', 'major', 'great'], right=False, include_lowest=True)
    df_clean['times'] = [1] * len(df_clean['mag'])
    df_merge = df_clean[['mag', 'region', 'times']]
    df_final = df_merge.groupby(['mag','region']).count().reset_index('mag').dropna().sort_values(by='times',ascending=False).drop_duplicates(['mag'])
    df_final[['times']] = df_final[['times']].astype(int)
    print(df_final)
    
    return df_final


mag_region()
