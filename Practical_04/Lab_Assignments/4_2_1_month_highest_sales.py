# 4.2.1. Month with the Highest Total Sales

import pandas as pd

file_name = input()
df = pd.read_csv(file_name)

df['Total Sales'] = df['Quantity'] * df['Price']
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Total Sales'].sum()

best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
