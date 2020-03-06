import requests
import pandas as pd


def issues(repo):
c
    raw = requests.get(
       'https://api.github.com/repos/{}/issues'.format(repo))
    issues_df1 = pd.DataFrame(raw.json()).loc[ : , ['number', 'title']]
    issues_df2 = pd.DataFrame(raw.json()).loc[ : , 'user']
    print(issues_df)

    return issues_df


issues("numpy/numpy")
