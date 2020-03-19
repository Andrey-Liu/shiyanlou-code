import numpy as np
import pandas as pd

def caculate_w():
    df = pd.read_csv("nyc-east-river-bicycle-counts.csv")
    x=[]
    for i in range(30):
        x.append([1,df['Brooklyn Bridge'].tolist()[i]])

    x = np.matrix(x)
    y = np.matrix(df['Manhattan Bridge'].tolist()).reshape(30,1)
    wb = (x.T * x).I* x.T * y
    b = round(float(wb[0]), 2)
    w = round(float(wb[1]), 2)
    print(w, b)
    return w, b

caculate_w()
