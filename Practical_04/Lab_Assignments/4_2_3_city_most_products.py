# 4.2.3. City that Sold the Most Products

import pandas as pd

file_name = input()
df = pd.read_csv(file_name)

city_sales = df.groupby('City')['Quantity'].sum()
best_city = city_sales.idxmax()

print(f"City sold the most products: {best_city}")
