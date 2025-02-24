import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(file_name, sheet_name):
    """Loads the dataset from an Excel file."""
    data = pd.ExcelFile(file_name)
    return data.parse(sheet_name)

def normalize_data(data):
    """Normalizes numeric columns using Min-Max Scaling."""
    scaler = MinMaxScaler()  # Initialize the Min-Max Scaler
    
    # Select only numeric columns for normalization
    numeric_data = data.select_dtypes(include='number')
    
    # Apply Min-Max Scaling and create a new DataFrame with the same column names
    normalized_data = pd.DataFrame(scaler.fit_transform(numeric_data), columns=numeric_data.columns)
    
    return normalized_data

def main():
    """Main function to execute the program."""
    file_name = 'Lab Session Data.xlsx'  # Excel file name
    sheet_name = 'thyroid0387_UCI'  # Sheet name

    # Load dataset
    thyroid_data = load_data(file_name, sheet_name)

    # Normalize numeric data
    thyroid_data_normalized = normalize_data(thyroid_data)

    # Display first few rows of normalized data
    print("Normalized Data:\n", thyroid_data_normalized.head())

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
