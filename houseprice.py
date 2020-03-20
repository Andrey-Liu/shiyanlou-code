import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt

def beijing(n):
    df = pd.read_csv("beijing_house_price.csv")
    df_clean = df.drop_duplicates().reset_index(drop=True)
    X = df_clean.iloc[:,[1,2,5]].values
    y = df_clean.iloc[:,10].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 10)
    
    model = LinearRegression()  
    model.fit(X_train, y_train)   
    b = model.intercept_
    
    X_train = X_train.reshape(len(X_train), 3)
    X_test = X_test.reshape(len(X_test), 3)
    y_train = y_train.reshape(len(y_train), 1)


    model = make_pipeline(PolynomialFeatures(
        n, include_bias=False), LinearRegression())
    model.fit(X_train, y_train)
    #b = model.intercept_
    pre_y = model.predict(X_test)
    mae = mean_absolute_error(y_test, pre_y.flatten())
    

    print(mae)


    return mae

beijing(5)
