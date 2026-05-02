# 3.2.3. NumPy: Custom Sequence Generation

import numpy as np

start = int(input())
stop = int(input())
step = int(input())

arr = np.arange(start, stop, step)
print(arr)
