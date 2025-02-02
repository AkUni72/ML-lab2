import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.ExcelFile('Lab Session Data.xlsx')
thyroid_data = data.parse('thyroid0387_UCI')

scaler = MinMaxScaler()
thyroid_data_normalized = pd.DataFrame(scaler.fit_transform(thyroid_data.select_dtypes(include='number')),
    columns=thyroid_data.select_dtypes(include='number').columns)

print("Normalized Data:\n", thyroid_data_normalized.head())
