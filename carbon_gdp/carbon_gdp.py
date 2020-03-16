import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns 
from sklearn.preprocessing import MinMaxScaler


def clean():
    data = pd.read_excel("ClimateChange.xlsx", sheet_name="Data")
    
    #data_gdp
    data_gdp = data[data['Series code'] == 'NY.GDP.MKTP.CD'].set_index('Country code')
    data_gdp.drop(labels=['Country name', 'Series code', 'Series name', 'SCALE', 'Decimals'], axis=1, inplace=True)
    data_gdp.replace('..', pd.np.NaN, inplace=True)
    data_gdp = data_gdp.fillna(method='bfill', axis=1).fillna(method='ffill', axis=1).fillna(0)
    data_gdp['GDP-SUM'] = data_gdp.sum(axis=1)
    data_gdp = data_gdp[['GDP-SUM']]
    
    #data_co2
    data_co2 = data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    data_co2.drop(labels=['Country name', 'Series code', 'Series name', 'SCALE', 'Decimals'], axis=1, inplace=True)
    data_co2.replace('..', pd.np.NaN, inplace=True)
    data_co2 = data_co2.fillna(method='bfill', axis=1).fillna(method='ffill', axis=1).fillna(0)
    data_co2['CO2-SUM'] = data_co2.sum(axis=1)
    data_co2 = data_co2[['CO2-SUM']]

    #merge
    df_clean = pd.concat([data_co2, data_gdp], axis=1)
     
    return df_clean

def min_max(df):
    df_min_max = (df - df.min()) / (df.max() - df.min())
    return df_min_max

def co2_gdp_plot():
    df_clean = clean()
    df_max_min = min_max(df_clean)
    #take information of China
    china = []
    for i in df_max_min[df_max_min.index == 'CHN'].values:
        china.extend(np.round(i, 3).tolist())

    #make figrue
    countries_labels = ['USA', 'CHN', 'FRA', 'RUS', 'GBR']
    sticks_labels = []
    labels_position = []
    
    for i in range(len(df_max_min)):
        if df_max_min.index[i] in countries_labels:
            sticks_labels.append(df_max_min.index[i])
            labels_position.append(i)
    
    fig, axes = plt.subplots()
    df_max_min.plot(
        kind='line',
        title='GDP-CO2',
        ax=axes
    )
    plt.xlabel("Countries")
    plt.ylabel("Values")
    plt.xticks(labels_position, sticks_labels, rotation='vertical')
    plt.show()
    print(china)
    
    return axes, china

co2_gdp_plot()

