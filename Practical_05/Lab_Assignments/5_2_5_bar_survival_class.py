# 5.2.5. Bar Plot for Survival by Class

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

survival_pclass = data.groupby(['Pclass', 'Survived']).size().unstack()
survival_pclass.plot(kind='bar', stacked=True)

plt.title("Survival by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.legend(["Not Survived", "Survived"])

plt.show()
