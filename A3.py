import pandas as pd

def load_excel_data(file_name, sheet_name):
    """Loads Excel data from a given file and sheet."""
    data = pd.ExcelFile(file_name)
    return data.parse(sheet_name)

def categorize_customers(data, threshold=200):
    """Categorizes customers as 'RICH' or 'POOR' based on payment amount."""
    payment_values = data['Payment (Rs)']  # Extract payment values
    customer_types = ['RICH' if amount > threshold else 'POOR' for amount in payment_values]  
    data['Customer Type'] = customer_types  # Add new column
    return data

def main():
    """Main function to execute the program."""
    file_name = 'Lab Session Data.xlsx'  # Excel file name
    sheet_name = 'Purchase data'  # Sheet name

    # Load data
    purchase_data = load_excel_data(file_name, sheet_name)

    # Categorize customers
    categorized_data = categorize_customers(purchase_data)

    # Print results
    print(categorized_data[['Customer', 'Payment (Rs)', 'Customer Type']])

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
