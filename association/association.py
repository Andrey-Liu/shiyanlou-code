import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def deal(data):
        return data.dropna().tolist()
    
    
def rule():
    data = pd.read_csv('shopping_data.csv', header=None)
    df_arr = data.apply(deal,axis=1).tolist()
    
    te = TransactionEncoder()  # ????
    te_ary = te.fit_transform(df_arr)  # ?????
    df = pd.DataFrame(te_ary, columns=te.columns_)
    
    frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
    
    association_rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)

    return frequent_itemsets, association_rule # ?????????????? DataFrame

rule()
