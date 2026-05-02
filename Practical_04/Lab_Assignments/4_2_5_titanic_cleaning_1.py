# 4.2.5. Titanic Dataset Analysis and Data Cleaning

import pandas as pd
import numpy as np

data = pd.read_csv('Titanic-Dataset.csv')

print(data.head())
print(data.tail())
print(data.shape)
print(data.info())
print(data.describe())
print(data.isnull().sum())

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop(columns='Cabin', inplace=True)
data["FamilySize"] = data['SibSp'] + data['Parch']
