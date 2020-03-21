import pandas as pd
import numpy as np

def gradient_descent():
    
    df = pd.read_csv("nyc-east-river-bicycle-counts.csv")
    x = df['Brooklyn Bridge'].values
    y = df['Manhattan Bridge'].values
    n = len(y)
    
    w = 0  # ????? 0
    b = 0  # ????? 0

    lr = 0.000000001# ???????
    num_iter = 1000# ????????

    for i in range(num_iter):  # ??????

        g1 = sum(x * (y - (w * x + b))) * (-2) / n
        g2 = sum(y - (w * x + b)) * (-2) / n
        w -= lr * g1
        b -= lr * g2

    return w, b
gradient_descent()
