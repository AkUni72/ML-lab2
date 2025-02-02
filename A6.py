import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

thyroid_data = pd.read_excel('Lab Session Data.xlsx', sheet_name='thyroid0387_UCI')

missing_values = thyroid_data.isna().sum()
print("\nMissing Values Per Column Before Imputation:")
print(missing_values[missing_values > 0])

numeric_data = thyroid_data.select_dtypes(include=np.number)
plt.figure(figsize=(12, 6))
sns.boxplot(data=numeric_data)
plt.title("Boxplot of Numeric Attributes (Outliers Detection)")
plt.xticks(rotation=45)
plt.show()

for col in thyroid_data.columns:
    if thyroid_data[col].dtype == 'object':
        mode_value = thyroid_data[col].mode()[0]
        thyroid_data[col].fillna(mode_value, inplace=True)
    else:
        if thyroid_data[col].skew() > 1 or thyroid_data[col].skew() < -1:
            thyroid_data[col].fillna(thyroid_data[col].median(), inplace=True)
        else:
            thyroid_data[col].fillna(thyroid_data[col].mean(), inplace=True)

print("\nMissing Values Per Column After Imputation:")
print(thyroid_data.isna().sum())
