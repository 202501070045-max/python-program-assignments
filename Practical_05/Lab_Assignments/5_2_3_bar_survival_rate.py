# 5.2.3. Bar Plot of Survival Rate of Passengers

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

survival_counts = data['Survived'].value_counts().sort_index()
survival_counts.plot(kind='bar')

plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")

plt.show()
