# 3.2.2. NumPy Horizontal and Vertical Stacking of Arrays

import numpy as np

print("Enter Array1:")
arr1 = np.array([list(map(int, input().split())) for i in range(3)])
print("Enter Array2:")
arr2 = np.array([list(map(int, input().split())) for i in range(3)])

h_stack = np.hstack((arr1, arr2))
v_stack = np.vstack((arr1, arr2))

print("Horizontal Stack:")
print(h_stack)
print("Vertical Stack:")
print(v_stack)
