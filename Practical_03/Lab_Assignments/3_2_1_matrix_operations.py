# 3.2.1. NumPy: Matrix Operations

import numpy as np

print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])
print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])

print("Addition (A + B):")
print(matrix_a + matrix_b)

print("Subtraction (A - B):")
print(matrix_a - matrix_b)

print("Element-wise Multiplication (A * B):")
print(matrix_a * matrix_b)

print("A dot B:")
print(np.dot(matrix_a, matrix_b))

print("Transpose of A:")
print(np.transpose(matrix_a))
