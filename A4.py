import pandas as pd
import statistics
import matplotlib.pyplot as plt
import seaborn as sns

def load_stock_data(file_name, sheet_name):
    """Loads stock data from an Excel file and processes date-related information."""
    stock_data = pd.read_excel(file_name, sheet_name=sheet_name)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])  # Convert date column to datetime
    stock_data['Day'] = stock_data['Date'].dt.day_name()  # Extract day name
    stock_data['Month'] = stock_data['Date'].dt.month  # Extract month number
    return stock_data

def compute_statistics(stock_data):
    """Computes mean and variance of stock prices."""
    mean_price = statistics.mean(stock_data['Price'])
    variance_price = statistics.variance(stock_data['Price'])
    print("Mean Price:", mean_price)
    print("Variance of Price:", variance_price)
    return mean_price

def analyze_wednesdays(stock_data, mean_price):
    """Computes sample mean for Wednesdays and its difference from the population mean."""
    wednesday_prices = stock_data[stock_data['Day'] == 'Wednesday']['Price']
    mean_wednesday = wednesday_prices.mean()
    print("Sample Mean of Prices on Wednesdays:", mean_wednesday)
    print(f"Difference from Population Mean: {abs(mean_price - mean_wednesday)}")

def analyze_april(stock_data, mean_price):
    """Computes sample mean for April and its difference from the population mean."""
    april_prices = stock_data[stock_data['Month'] == 4]['Price']
    mean_april = april_prices.mean()
    print("Sample Mean of Prices in April:", mean_april)
    print(f"Difference from Population Mean: {abs(mean_price - mean_april)}")

def compute_probabilities(stock_data):
    """Computes probability of making a loss and conditional probability of profit on Wednesdays."""
    loss_probability = (stock_data['Chg%'] < 0).mean()
    print(f"Probability of making a loss: {loss_probability:.2%}")

    wednesday_prices = stock_data[stock_data['Day'] == 'Wednesday']['Price']
    profit_wednesday = stock_data[(stock_data['Day'] == 'Wednesday') & (stock_data['Chg%'] > 0)]
    profit_wednesday_prob = len(profit_wednesday) / len(wednesday_prices) if len(wednesday_prices) > 0 else 0
    print(f"Probability of Profit on Wednesdays: {profit_wednesday_prob:.2%}")

    conditional_prob = profit_wednesday_prob  # Since we already handled division above
    print(f"Conditional Probability (Profit | Wednesday): {conditional_prob:.2%}")

def plot_change_percentage(stock_data):
    """Plots a scatter plot of Chg% against the day of the week."""
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=stock_data, x='Day', y='Chg%', hue='Chg%', palette="coolwarm", alpha=0.7)
    plt.title('Chg% vs Day of the Week')
    plt.xticks(rotation=45)
    plt.show()

def main():
    """Main function to execute the program."""
    file_name = 'Lab Session Data.xlsx'  # Excel file name
    sheet_name = 'IRCTC Stock Price'  # Sheet name

    # Load and process stock data
    stock_data = load_stock_data(file_name, sheet_name)

    # Compute statistics
    mean_price = compute_statistics(stock_data)

    # Perform analyses
    analyze_wednesdays(stock_data, mean_price)
    analyze_april(stock_data, mean_price)

    # Compute probabilities
    compute_probabilities(stock_data)

    # Plot data
    plot_change_percentage(stock_data)

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
