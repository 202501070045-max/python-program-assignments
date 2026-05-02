# 1.2.4. Pattern-2 (Right-angled triangle of numbers)

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")
