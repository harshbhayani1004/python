import pandas as pd

df = pd.read_csv("employee.csv")

numeric_cols = df.select_dtypes(include='number').columns

df[numeric_cols[0]].describe()

corr = df[numeric_cols[0]].corr(df[numeric_cols[1]])

print(f"Correlation between {numeric_cols[0]} and {numeric_cols[1]}: {corr}")

print(df[numeric_cols[:3]].corr())