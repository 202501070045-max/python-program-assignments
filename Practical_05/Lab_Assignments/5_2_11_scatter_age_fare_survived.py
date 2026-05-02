# 5.2.11. Scatter Plot for Age vs Fare by Survived

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Color mapping: 0 -> 'red', 1 -> 'blue'
colors = data['Survived'].map({0: 'red', 1: 'blue'})

plt.scatter(data['Age'], data['Fare'], c=colors)

plt.title("Age vs. Fare by Survival")
plt.xlabel("Age")
plt.ylabel("Fare")

plt.show()
