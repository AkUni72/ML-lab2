import pandas as pd

# Loads Excel data from a given file and sheet
def load_excel_data(file_name, sheet_name):
    excel_data = pd.ExcelFile(file_name)
    return excel_data.parse(sheet_name)

# Extracts matrix A  and C 
def extract_matrices(data):
    A = data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']]  # Feature matrix
    C = data[['Payment (Rs)']]  # Target matrix
    return A, C

# Prints matrices and their properties
def print_matrix_info(A, C):
    print("Matrix A:")
    print(A)
    print("Matrix C:")
    print(C)

    # Compute and print dimensionality
    dimensionality = A.shape[1]
    print("Dimensionality of the vector space:", dimensionality)

    # Compute and print number of vectors
    num_vectors = A.shape[0]
    print("Number of vectors in the vector space:", num_vectors)

def main():
    """Main function to execute the program."""
    file_name = 'Lab Session Data.xlsx'  # Excel file name
    sheet_name = 'Purchase data'  # Sheet name

    # Load data
    purchase_data = load_excel_data(file_name, sheet_name)

    # Extract matrices
    A, C = extract_matrices(purchase_data)

    # Print matrix details
    print_matrix_info(A, C)

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
