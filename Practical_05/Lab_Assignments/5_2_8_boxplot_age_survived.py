# 5.2.8. Box Plot for Age by Survived

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

data.boxplot(column='Age', by='Survived')

plt.title("Age by Survival")
plt.suptitle('')
plt.xlabel("Survived")
plt.ylabel("Age")

plt.show()
