import pandas as pd
import os

os.chdir("/home/beehyv/Downloads/python/python_basics")
data = pd.read_csv("sample_csv1.csv")  # Get data in a object
# print(data) # To print whole data
# print(data.head(2)) # To return top n (5 by default) rows of a data frame
# print(data.columns.tolist())  # To return all column names
# print(data.loc[[1], ['P_ID', 'P_Name']])  # To return specific columns and rows 1,3
# data2 = pd.read_excel('sample_excel.xlsx')
# print(data2.loc[[1], ['id', ' block_id']])
