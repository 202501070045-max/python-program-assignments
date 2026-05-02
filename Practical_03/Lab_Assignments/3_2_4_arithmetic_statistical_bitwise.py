# 3.2.4. NumPy: Arithmetic, Statistical, and Bitwise Operations

import numpy as np

def array_operations(A, B):
    arr_A = np.array(A)
    arr_B = np.array(B)

    # Arithmetic Operations
    sum_result = np.add(arr_A, arr_B)
    diff_result = np.subtract(arr_A, arr_B)
    prod_result = np.multiply(arr_A, arr_B)

    # Statistical Operations
    mean_A = np.mean(arr_A)
    median_A = np.median(arr_A)
    std_dev_A = np.std(arr_A)

    # Bitwise Operations
    and_result = np.bitwise_and(arr_A, arr_B)
    or_result = np.bitwise_or(arr_A, arr_B)
    xor_result = np.bitwise_xor(arr_A, arr_B)

    print("Element-wise Sum:", ' '.join(map(str, sum_result)))
    print("Element-wise Difference:", ' '.join(map(str, diff_result)))
    print("Element-wise Product:", ' '.join(map(str, prod_result)))
    print(f"Mean of A: {mean_A}")
    print(f"Median of A: {median_A}")
    print(f"Standard Deviation of A: {std_dev_A}")
    print("Bitwise AND:", ' '.join(map(str, and_result)))
    print("Bitwise OR:", ' '.join(map(str, or_result)))
    print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))
B = list(map(int, input().split()))
array_operations(A, B)
