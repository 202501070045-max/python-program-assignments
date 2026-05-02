# 4.2.2. Best Selling Product

import pandas as pd

file_name = input()
df = pd.read_csv(file_name)

product_quantity = df.groupby('Product')['Quantity'].sum()

best_product = product_quantity.idxmax()
highest_quantity = product_quantity.max()

print(f"Best selling product: {best_product}")
print(f"Total quantity sold: {highest_quantity}")
