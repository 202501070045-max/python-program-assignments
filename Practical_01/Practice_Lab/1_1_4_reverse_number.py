# 1.1.4. Reverse a Number

# Method 1: Loop-based
n = int(input())
reversed_num = 0
temp = n
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10
print(reversed_num)

# Method 2: Pythonic way (commented out)
# num = int(input())
# reversed_num = int(str(num)[::-1])
# print(reversed_num)
