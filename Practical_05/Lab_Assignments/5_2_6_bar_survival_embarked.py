# 5.2.6. Bar Plot for Survival by Embarked

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

survival_embarked = data.groupby(['Embarked_Q', 'Survived']).size().unstack()
survival_embarked.plot(kind='bar', stacked=True)

plt.title("Survival by Embarked")
plt.xlabel("Embarked")
plt.ylabel("Count")
plt.legend(["Not Survived", "Survived"])

plt.show()
