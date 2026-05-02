# 4.2.4. Most Frequently Sold Product Pairs

import pandas as pd
from itertools import combinations
from collections import Counter

file_name = input()
df = pd.read_csv(file_name)

daily_transactions = df.groupby('Date')['Product'].apply(list)

pair_counts = Counter()

for products in daily_transactions:
    products = sorted(products)
    pairs = list(combinations(products, 2))
    pair_counts.update(pairs)

if pair_counts:
    max_count = max(pair_counts.values())
    for pair, count in pair_counts.items():
        if count == max_count:
            print(f"{pair[0]} and {pair[1]}: {count} times")
else:
    print("No product pairs found.")
