# 1.2.2. Fibonacci Series using Recursive Function

def fibonacci(n):
    if n <= 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
for i in range(1, n + 1):
    print(fibonacci(i), end=" ")
