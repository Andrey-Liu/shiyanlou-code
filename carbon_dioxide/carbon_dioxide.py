import numpy as np
import pandas as pd

def co2():

    #read excel
    Data = pd.read_excel("ClimateChange.xlsx", sheet_name=0)
    Country = pd.read_excel("ClimateChange.xlsx", sheet_name=1)
    Data_1 = Data[Data['Series code'] == 'EN.ATM.CO2E.KT']
    Data_2 = pd.merge(Data_1, Country, on=['Country code', 'Country name'])
    Data_2.drop(labels=['Country code', 'Series code', 'SCALE', 'Decimals', 'Capital city', 'Region', 'Lending category'], axis=1, inplace=True)
    Data_2.replace({'..', np.nan}, inplace=True)
    Data_2.drop(Data_4[Data_4.isna().sum(axis=1) == 22].index.tolist(), axis=0, inplace=True)
    #????
    relocat = Data_2['Income group']
    Data_2.drop(labels=['Income group'], axis=1,inplace = True)
    Data_2.insert(0, 'Income group', relocat)
    Data_6 = Data_2.fillna(method="bfill",axis=1).fillna(method='pad',axis=1)
    #???????
    Data_6['Sum emissions'] = 0
    for i in range(3,25):
        Data_6['Sum emissions'] += Data_6.iloc[:,i]
    #?????????????????
    Data_7 = Data_6.groupby(['Income group', 'Country name'])[['Sum emissions']].sum().sort_values(by=['Sum emissions'], ascending=False,inplace=False).reset_index().drop_duplicates(['Income group'],keep='first', inplace=False)
    Data2 =Data_7.rename(columns={"Country name" : "Highest emission country", "Sum emissions" : "Highest emissions"})
    #?????????????????
    Data_8 = Data_6.groupby(['Income group', 'Country name'])[['Sum emissions']].sum().sort_values(by=['Sum emissions'], ascending=True, inplace=False).reset_index().drop_duplicates(['Income group'],keep='first', inplace=False)
    Data3 =Data_8.rename(columns={"Country name" : "Lowest emission country", "Sum emissions" : "Lowest emissions"})
    #?????????
    Data1 = Data_6.groupby(['Income group'])[['Sum emissions']].sum().reset_index()
    #???
    Data_all = pd.merge(Data1, Data2, on=['Income group'])
    results = pd.merge(Data_all, Data3, on=['Income group']).set_index('Income group')
    print(results)
    return results

co2()
    
