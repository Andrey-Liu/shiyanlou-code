import sqlite3
import pandas as pd


def count(file, id):
    
    sql_con = sqlite3.connect(file)
    sql_query = "select sum(minutes) from data where user_id = {}".format(id)
    sum_minutes_df = pd.read_sql(sql_query, sql_con)
    sum_minutes = sum_minutes_df.at[0,'sum(minutes)']
    if sum_minutes == None:
        sum_minutes = 0
        print(sum_minutes)
    else:
        print(sum_minutes)
    return sum_minutes

count("users_data.sqlite", 8490)
