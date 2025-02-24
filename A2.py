import pandas as pd
import numpy as np
from numpy.linalg import pinv

def load_excel_data(file_name, sheet_name):
    """Loads Excel data from a given file and sheet."""
    data = pd.ExcelFile(file_name)
    return data.parse(sheet_name)

def extract_matrices(data):
    """Extracts matrix A (features) and matrix C (target variable), handling missing values."""
    A = data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].dropna()  # Feature matrix
    C = data[['Payment (Rs)']]  # Target matrix
    return A, C

def compute_model_vector(A, C):
    """Computes the model vector X using the pseudo-inverse."""
    return np.dot(pinv(A), C)

def main():
    """Main function to execute the program."""
    file_name = 'Lab Session Data.xlsx'  # Excel file name
    sheet_name = 'Purchase data'  # Sheet name

    # Load data
    purchase_data = load_excel_data(file_name, sheet_name)

    # Extract matrices
    A, C = extract_matrices(purchase_data)

    # Compute model vector
    X = compute_model_vector(A, C)

    # Print results
    print("Model vector X (Cost per product):\n", X)

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
