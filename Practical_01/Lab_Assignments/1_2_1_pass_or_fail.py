# 1.2.1. Pass or Fail

n = int(input())
marks = list(map(int, input().split()))

if any(m < 40 for m in marks):
    print("Fail")
else:
    aggregate_percentage = sum(marks) / n

    if aggregate_percentage > 75:
        grade = "Distinction"
    elif 60 <= aggregate_percentage < 75:
        grade = "First Division"
    elif 50 <= aggregate_percentage < 60:
        grade = "Second Division"
    elif 40 <= aggregate_percentage < 50:
        grade = "Third Division"
    else:
        grade = "Fail"

    print(f"Aggregate Percentage: {aggregate_percentage:.2f}")
    print(f"Grade: {grade}")
