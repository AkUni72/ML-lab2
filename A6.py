import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_name, sheet_name):
    """Loads the dataset from an Excel file."""
    return pd.read_excel(file_name, sheet_name=sheet_name)

def check_missing_values(data, message="Missing Values Per Column:"):
    """Checks for missing values in the dataset and prints the columns with missing values."""
    missing_values = data.isna().sum()  # Count missing values per column
    print(f"\n{message}")
    print(missing_values[missing_values > 0])  # Print only columns with missing values

def plot_boxplot(data):
    """Plots a boxplot for numeric attributes to detect outliers."""
    numeric_data = data.select_dtypes(include=np.number)  # Extract numeric data
    plt.figure(figsize=(12, 6))  # Set figure size
    sns.boxplot(data=numeric_data)  # Create boxplot
    plt.title("Boxplot of Numeric Attributes (Outliers Detection)")
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.show()

def impute_missing_values(data):
    """Handles missing values using mode for categorical and mean/median for numerical attributes."""
    for col in data.columns:
        if data[col].dtype == 'object':  # For categorical columns
            mode_value = data[col].mode()[0]  # Get the most frequent value
            data[col].fillna(mode_value, inplace=True)  # Fill missing values with mode
        else:  # For numeric columns
            skewness = data[col].skew()  # Calculate skewness
            if skewness > 1 or skewness < -1:  # Highly skewed data
                data[col].fillna(data[col].median(), inplace=True)  # Use median for skewed data
            else:
                data[col].fillna(data[col].mean(), inplace=True)  # Use mean for normally distributed data

def main():
    """Main function to execute the program."""
    file_name = 'Lab Session Data.xlsx'  # Excel file name
    sheet_name = 'thyroid0387_UCI'  # Sheet name

    # Load dataset
    thyroid_data = load_data(file_name, sheet_name)

    # Check missing values before imputation
    check_missing_values(thyroid_data, "Missing Values Per Column Before Imputation:")

    # Detect outliers using boxplot
    plot_boxplot(thyroid_data)

    # Perform missing value imputation
    impute_missing_values(thyroid_data)

    # Check missing values after imputation
    check_missing_values(thyroid_data, "Missing Values Per Column After Imputation:")

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
