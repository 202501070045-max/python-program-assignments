# 3.1.1. Numpy Array Operations

import numpy as np

r, c = map(int, input().split())

elements = []
for _ in range(r):
    row = list(map(int, input().split()))
    elements.extend(row)

arr = np.array(elements)
reshaped_arr = arr.reshape(r, c)

print(reshaped_arr)
print(reshaped_arr.ndim)
print(reshaped_arr.shape)
print(reshaped_arr.size)
