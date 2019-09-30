import numpy as np
import pandas as pd


df = pd.DataFrame([[6, 2, 6, 0],
                   [3, 4, 9, 1],
                   [6, 6, 4, 5],
                   [1, 1, 5, 5]],
                  columns=list('ABCD'))

# df['new_col'] = 5
# test = df['new_col']

# df.insert(1, 'Col2', 999)

print(df.columns)

print(df.iloc[:, -1:])
# df = df.iloc[:, 1:-1]
# print(df.iloc[:, 2:3].columns())
# columns = df.columns.values.tolist()
# training_df = df[df['A'] != 3]
# print(df)