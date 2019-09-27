import numpy as np
import pandas as pd


df = pd.DataFrame([[6, 2, 6, 0],
                   [3, 4, 9, 1],
                   [6, 6, 4, 5],
                   [6, 3, 8, 4]],
                  columns=list('ABCD'))

print(df)
print(df.iloc[:, 2:3])

