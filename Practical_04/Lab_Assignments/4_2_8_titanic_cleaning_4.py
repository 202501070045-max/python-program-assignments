# 4.2.8. Titanic Dataset Analysis and Data Cleaning - 4

import pandas as pd
import numpy as np

data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Survivors by gender
print(data[data['Survived'] == 1]['Sex'].value_counts())

# 2. Non-survivors by gender
print(data[data['Survived'] == 0]['Sex'].value_counts())

# 3. Survivors by embarked location
print(data[data['Survived'] == 1]['Embarked_S'].value_counts())

# 4. Non-survivors by embarked location
print(data[data['Survived'] == 0]['Embarked_S'].value_counts())

# 5. Percentage of children (Age < 18) who survived
print(data[data['Age'] < 18]['Survived'].mean())

# 6. Percentage of adults (Age >= 18) who survived
print(data[data['Age'] >= 18]['Survived'].mean())

# 7. Median age of survivors
print(data[data['Survived'] == 1]['Age'].median())

# 8. Median age of non-survivors
print(data[data['Survived'] == 0]['Age'].median())

# 9. Median fare of survivors
print(data[data['Survived'] == 1]['Fare'].median())

# 10. Median fare of non-survivors
print(data[data['Survived'] == 0]['Fare'].median())
