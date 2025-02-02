import pandas as pd

excel_data = pd.ExcelFile('Lab Session Data.xlsx')
purchase_data = excel_data.parse('Purchase data')

A = purchase_data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']]
C = purchase_data[['Payment (Rs)']]

print("Matrix A:")
print(A)
print("Matrix C:")
print(C)

dimensionality = A.shape[1]
print("Dimensionality of the vector space: ",dimensionality)

num_vectors = A.shape[0]
print("Number of vectors in the vector space: ",num_vectors)