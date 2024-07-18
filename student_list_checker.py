import pandas as pd

df = pd.read_csv('students.csv')

row_5 = df.iloc[5]

print(row_5)