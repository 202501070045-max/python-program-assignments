# 4.1.1. Pandas – Series Creation and Manipulation

import pandas as pd

numbers = list(map(int, input().split()))

series = pd.Series(numbers)

grouped = series.groupby(series % 2 == 0).mean()

grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]

print("Mean of even and odd numbers:")
print(grouped)
