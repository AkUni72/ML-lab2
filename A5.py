import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

thyroid_data = pd.read_excel('Lab Session Data.xlsx', sheet_name='thyroid0387_UCI')

print("Dataset Information:")
print(thyroid_data.info())
print("\nFirst 5 Rows of the Dataset:")
print(thyroid_data.head())

for col in thyroid_data.columns:
    unique_values = thyroid_data[col].nunique()
    dtype = thyroid_data[col].dtype
    if dtype == 'object':
        print(f"{col}: Nominal (Categorical) with {unique_values} unique values")
    elif unique_values < 10:
        print(f"{col}: Ordinal (Categorical) with {unique_values} unique values")
    else:  
        print(f"{col}: Numeric")

categorical_columns = thyroid_data.select_dtypes(include=['object']).columns
print("\nCategorical Columns to be Encoded:")
print(list(categorical_columns))

numeric_data = thyroid_data.select_dtypes(include=np.number)
print("\nSummary Statistics for Numeric Attributes:")
print(numeric_data.describe())

missing_values = thyroid_data.isna().sum()
print("\nMissing Values Per Column:")
print(missing_values[missing_values > 0])

plt.figure(figsize=(12, 6))
sns.boxplot(data=numeric_data)
plt.title("Boxplot of Numeric Attributes (Outliers Detection)")
plt.xticks(rotation=45)
plt.show()

mean_values = numeric_data.mean()
std_values = numeric_data.std()
print("\nMean of Numeric Attributes:\n", mean_values)
print("\nStandard Deviation of Numeric Attributes:\n", std_values)
