#
# Syafiera
# Add missing value
#

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

# Add missing values
df2 = df.copy()
df2.loc[2:5, 'Pregnancies'] = None
df2.head(10)
print(df2.head(10))

# Add missing values
df2.isnull().sum()
df2.shape

# Remove rows with missing value
df3 = df2.copy()
df3 = df3.dropna()
print(df3.shape)

# Creating new columns based on other columns
df2['Glucose_Insulin_Ratio'] = df2['Glucose']/df2['Insulin']
df2.head(10)
print(df2.head(10))

# Count by value
df['Outcome'].value_counts()
df['Outcome'].value_counts(sort=False)

# By group 
df.groupby('Outcome').mean()
print(df.groupby('Outcome').mean())

# By group
df.groupby(['Pregnancies', 'Outcome']).mean()
print(df.groupby(['Pregnancies', 'Outcome']).mean())

df[['BMI', 'Glucose']].plot.line(figsize=(20, 10),
                                 color={"BMI": "red", "Glucose": "blue"})
plt.title('Syafiera')
plt.show()

