# 5.2.9. Box Plot for Fare by Pclass

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

data.boxplot(column='Fare', by='Pclass')

plt.title("Fare by Pclass")
plt.suptitle('')
plt.xlabel("Pclass")
plt.ylabel("Fare")

plt.show()
