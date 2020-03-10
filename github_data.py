import requests
import pandas as pd


def issues(repo):
    raw = requests.get(
       'https://api.github.com/repos/{}/issues'.format(repo))

    issues_df1 = pd.DataFrame(raw.json())
    issues_df2 = pd.DataFrame(raw.json()).loc[ : , 'user']
    issues_df = issues_df1.loc[:, ('number', 'title','user_name')]
    for i in range(0,30):
        issues_df.loc[i,'user_name']= issues_df2.loc[i,]['login']

    return issues_df


issues("numpy/numpy")
