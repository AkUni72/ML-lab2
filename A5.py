import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_name, sheet_name):
    """Loads the dataset from an Excel file."""
    return pd.read_excel(file_name, sheet_name=sheet_name)

def display_dataset_info(data):
    """Displays dataset information and the first few rows."""
    print("Dataset Information:")
    print(data.info())  # Print dataset structure, column types, and memory usage
    print("\nFirst 5 Rows of the Dataset:")
    print(data.head())  # Show the first 5 rows for quick inspection

def classify_columns(data):
    """Classifies columns as Nominal, Ordinal, or Numeric based on unique values and data type."""
    for col in data.columns:
        unique_values = data[col].nunique()  # Count unique values
        dtype = data[col].dtype  # Get data type
        if dtype == 'object':
            print(f"{col}: Nominal (Categorical) with {unique_values} unique values")
        elif unique_values < 10:  # If fewer than 10 unique values, assume ordinal
            print(f"{col}: Ordinal (Categorical) with {unique_values} unique values")
        else:  
            print(f"{col}: Numeric")  # More unique values indicate a numeric feature

def get_categorical_columns(data):
    """Returns and prints a list of categorical columns."""
    categorical_columns = data.select_dtypes(include=['object']).columns
    print("\nCategorical Columns to be Encoded:")
    print(list(categorical_columns))  # Display categorical column names
    return categorical_columns

def display_numeric_summary(data):
    """Displays summary statistics (mean, min, max, std, etc.) for numeric attributes."""
    numeric_data = data.select_dtypes(include=np.number)  # Extract only numeric columns
    print("\nSummary Statistics for Numeric Attributes:")
    print(numeric_data.describe())  # Show summary statistics
    return numeric_data

def check_missing_values(data):
    """Checks for missing values in the dataset and prints columns that have missing values."""
    missing_values = data.isna().sum()  # Count missing values per column
    print("\nMissing Values Per Column:")
    print(missing_values[missing_values > 0])  # Print only columns with missing values

def plot_boxplot(data):
    """Plots a boxplot for numeric attributes to detect outliers."""
    plt.figure(figsize=(12, 6))  # Set figure size
    sns.boxplot(data=data)  # Create boxplot for numeric attributes
    plt.title("Boxplot of Numeric Attributes (Outliers Detection)")
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.show()

def compute_statistics(data):
    """Computes and prints the mean and standard deviation of numeric attributes."""
    mean_values = data.mean()  # Calculate mean for each numeric column
    std_values = data.std()  # Calculate standard deviation for each numeric column
    print("\nMean of Numeric Attributes:\n", mean_values)
    print("\nStandard Deviation of Numeric Attributes:\n", std_values)

def main():
    """Main function to execute the program."""
    file_name = 'Lab Session Data.xlsx'  # Excel file name
    sheet_name = 'thyroid0387_UCI'  # Sheet name

    # Load dataset
    thyroid_data = load_data(file_name, sheet_name)

    # Perform analyses
    display_dataset_info(thyroid_data)  # Display dataset structure and first few rows
    classify_columns(thyroid_data)  # Identify Nominal, Ordinal, and Numeric columns
    get_categorical_columns(thyroid_data)  # Identify categorical columns

    # Numeric data analysis
    numeric_data = display_numeric_summary(thyroid_data)  # Display statistics for numeric data
    check_missing_values(thyroid_data)  # Check for missing values in the dataset
    plot_boxplot(numeric_data)  # Plot boxplots to detect outliers
    compute_statistics(numeric_data)  # Compute mean and standard deviation for numeric attributes

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
