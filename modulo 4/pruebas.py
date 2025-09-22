import pandas as pd
import kagglehub
import os 
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\clases\modulo 4\clase 3\ai_job_dataset.csv")
print(df.head(5))

print('\n')
# print(df.groupby('salary_usd')['employee_residence'].describe())
# print('\n')

print(df.groupby('employee_residence')['salary_usd'].describe())
print('\n')


# sns.boxplot(x='employee_residence', y='salary_usd', data=df)
# plt.show()

sns.boxplot(x='salary_usd', y='employee_residence', data=df)
plt.show()
