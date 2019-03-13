import pandas as pd
import os
os.chdir("/home/beehyv/Downloads/python/Pandas")
data = pd.read_csv("sample_csv1.csv")  # Get data in a object
# print(data) # To print whole data
# print(data.head(2)) # To return top n (5 by default) rows of a data frame
# print(data.columns.tolist())  # To return all column names
# print(data.loc[[1], ['P_ID', 'P_Name']])  # To return specific columns and rows 1,3
