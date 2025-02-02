import pandas as pd
import numpy as np
from numpy.linalg import pinv

data = pd.ExcelFile('Lab Session Data.xlsx')
purchase_data = data.parse('Purchase data')

A = purchase_data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].dropna()
C = purchase_data[['Payment (Rs)']]

X = np.dot(pinv(A), C)

print("Model vector X (Cost per product):\n", X)