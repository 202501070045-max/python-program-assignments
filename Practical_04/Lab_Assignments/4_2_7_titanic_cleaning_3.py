# 4.2.7. Titanic Dataset Analysis and Data Cleaning - 3

import pandas as pd
import numpy as np

data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Survival rate by class
print(data.groupby('Pclass')['Survived'].mean())

# 2. Survival rate by embarkation location
print(data.groupby('Embarked_S')['Survived'].mean())

# 3. Survival rate by family size
print(data.groupby('FamilySize')['Survived'].mean())

# 4. Survival rate by being alone
print(data.groupby('IsAlone')['Survived'].mean())

# 5. Average fare by class
print(data.groupby('Pclass')['Fare'].mean())

# 6. Average age by class
print(data.groupby('Pclass')['Age'].mean())

# 7. Average age by survival status
print(data.groupby('Survived')['Age'].mean())

# 8. Average fare by survival status
print(data.groupby('Survived')['Fare'].mean())

# 9. Survivors by class
print(data[data['Survived'] == 1]['Pclass'].value_counts())

# 10. Non-survivors by class
print(data[data['Survived'] == 0]['Pclass'].value_counts())
