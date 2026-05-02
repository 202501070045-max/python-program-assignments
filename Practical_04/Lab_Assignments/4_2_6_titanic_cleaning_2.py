# 4.2.6. Titanic Dataset Analysis and Data Cleaning - 2

import pandas as pd
import numpy as np

data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']

# 1. IsAlone column
data['IsAlone'] = np.where(data['FamilySize'] == 0, 1, 0)

# 2. Convert Sex to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 3. One-hot encode Embarked
data = pd.get_dummies(data, columns=['Embarked'])

# 4. Mean age
mean_age = data['Age'].mean()
print(mean_age)

# 5. Median fare
median_fare = data['Fare'].median()
print(median_fare)

# 6. Passengers by class
print(data['Pclass'].value_counts())

# 7. Passengers by gender
print(data['Sex'].value_counts())

# 8. Passengers by survival status
print(data['Survived'].value_counts())

# 9. Overall survival rate
survival_rate = data['Survived'].mean()
print(format(survival_rate))

# 10. Survival rate by gender
survival_by_gender = data.groupby('Sex')['Survived'].mean()
print(survival_by_gender)
