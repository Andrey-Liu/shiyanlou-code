import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

def identify():

    df = pd.read_csv('banknote_train.csv')

    X_train= df[['variance', 'skewness']] 
    y_train = df['class']  
    X_test = pd.read_csv('banknote_test.csv')


    #model = KNeighborsClassifier()  # ????????
    model = SVC()
    model.fit(X_train, y_train)  # ????????????

    y_predict = model.predict(X_test)
    X_test['class']= pd.Series(y_predict)
    df_test = X_test

    
    return df_test

print(identify())

