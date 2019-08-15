import pandas as pd
import os

train_data_file_path = os.getcwd() + '/train.csv'
test_data_file_path = os.getcwd() + '/test.csv'

train_df = pd.read_csv(train_data_file_path, index_col='loan_id')
filter1 = train_df['m13'] == '1'
train_df.where(filter1, inplace=True)
print(train_df())


# 898126533464
