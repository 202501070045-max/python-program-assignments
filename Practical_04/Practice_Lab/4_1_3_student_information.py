# 4.1.3. Student Information

import pandas as pd

file = input()
data = pd.read_csv(file, sep=r"\s+", header=None, names=["Name", "Age", "Grade"])

print("First five rows:")
print(data.head())

average_age = data['Age'].mean()
print(f"Average age: {round(average_age, 2)}")

filtered_students = data[data['Grade'] <= 'B']
print("Students with a grade up to B")
print(filtered_students)
