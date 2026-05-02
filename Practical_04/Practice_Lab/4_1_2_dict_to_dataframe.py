# 4.1.2. Dictionary to DataFrame
# Note: df.append() is deprecated in newer pandas. Using pd.concat() instead.

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Adding a new row
new_name = input("New name: ")
new_age = int(input("New age: "))
new_row = pd.DataFrame({'Name': [new_name], 'Age': [new_age]})
df = pd.concat([df, new_row], ignore_index=True)
print("After adding a row:\n", df)

# Modifying a row
modify_index = int(input("Index of row to modify: "))
new_age = int(input("New age: "))
df.at[modify_index, 'Age'] = new_age
print("After modifying a row:")
print(df)

# Deleting a row
del_index = int(input("Index of row to delete: "))
df = df.drop(del_index).reset_index(drop=True)
print("After deleting a row:")
print(df)

# Adding a new column
genders = input("Enter genders separated by space: ").split()
df["Gender"] = genders
print("After adding a new column:")
print(df)

# Modifying a column
df['Name'] = df['Name'].str.upper()
print("After modifying a column:")
print(df)

# Deleting a column
df = df.drop(columns='Age').reset_index(drop=True)
print("After deleting a column:")
print(df)
