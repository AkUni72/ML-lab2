import pandas as pd
import statistics
import matplotlib.pyplot as plt
import seaborn as sns

stock_data = pd.read_excel('Lab Session Data.xlsx', sheet_name='IRCTC Stock Price')

stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data['Day'] = stock_data['Date'].dt.day_name()
stock_data['Month'] = stock_data['Date'].dt.month

mean_price = statistics.mean(stock_data['Price'])
variance_price = statistics.variance(stock_data['Price'])
print("Mean Price: ",mean_price)
print("Variance of Price: ",variance_price)

wednesday_prices = stock_data[stock_data['Day'] == 'Wednesday']['Price']
mean_wednesday = wednesday_prices.mean()
print("Sample Mean of Prices on Wednesdays: ",mean_wednesday)

print("Difference from Population Mean: {abs(mean_price - mean_wednesday)}")

april_prices = stock_data[stock_data['Month'] == 4]['Price']
mean_april = april_prices.mean()
print("Sample Mean of Prices in April: ",mean_april)

print(f"Difference from Population Mean: {abs(mean_price - mean_april)}")

loss_probability = (stock_data['Chg%'] < 0).mean()
print(f"Probability of making a loss: {loss_probability:.2%}")

profit_wednesday = stock_data[(stock_data['Day'] == 'Wednesday') & (stock_data['Chg%'] > 0)]
profit_wednesday_prob = len(profit_wednesday) / len(wednesday_prices)
print(f"Probability of Profit on Wednesdays: {profit_wednesday_prob:.2%}")

total_wednesdays = len(wednesday_prices)
profitable_wednesdays = len(profit_wednesday)
conditional_prob = profitable_wednesdays / total_wednesdays if total_wednesdays > 0 else 0
print(f"Conditional Probability (Profit | Wednesday): {conditional_prob:.2%}")

plt.figure(figsize=(10, 5))
sns.scatterplot(data=stock_data, x='Day', y='Chg%', hue='Chg%', palette="coolwarm", alpha=0.7)
plt.title('Chg% vs Day of the Week')
plt.xticks(rotation=45)
plt.show()