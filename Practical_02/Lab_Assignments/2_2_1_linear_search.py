# 2.2.1. Linear Search Technique

def main():
    numbers = list(map(int, input().split()))
    key = int(input())

    found = False
    for i in range(len(numbers)):
        if numbers[i] == key:
            print(i)
            found = True
            break

    if not found:
        print("Not found")

if __name__ == "__main__":
    main()
