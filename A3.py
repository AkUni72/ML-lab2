import pandas as pd

data = pd.ExcelFile('Lab Session Data.xlsx')
purchase_data = data.parse('Purchase data')

payment_values = purchase_data['Payment (Rs)']
customer_types = ['RICH' if amount > 200 else 'POOR' for amount in payment_values]
purchase_data['Customer Type'] = customer_types

print(purchase_data[['Customer', 'Payment (Rs)', 'Customer Type']])
