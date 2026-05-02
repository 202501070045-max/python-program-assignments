# 1.1.2. Conditional Calculation based on the Number of Digits
# Constraints: 1 <= n <= 999

n = int(input())

if n < 1 or n >= 1000:
    print("Invalid")
elif n < 10:
    print(n ** 2)
elif n < 100:
    print(f"{n ** 0.5:.2f}")
else:
    print(f"{n ** (1/3):.2f}")
