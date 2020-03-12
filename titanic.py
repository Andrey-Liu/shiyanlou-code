from matplotlib import pyplot as plt
import seaborn as sns

def plot():
    df = sns.load_dataset("titanic")
    fig ,axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 5))
    
    sns.distplot(df.dropna(how='any', axis=0, subset=['age'])['age'], ax=axes[0])
    sns.countplot(x="sex", hue="alive", data=df, ax=axes[1])
    sns.countplot(x="class", hue="alive", data=df, ax=axes[2]) 
    
    plt.show()
    
    return axes

plot()
