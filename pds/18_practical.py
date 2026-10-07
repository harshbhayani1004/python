import pandas as pd
import numpy as np

data = {
    "Name": ["Harsh", "Ashish", "Meet", "Taksh", "Harsh", "Darsh", "Aryan"],
    "Age": [20, np.nan, 21, 22, 20, 19, 23],
    "Score": [87, 91, np.nan, 74, 87, 68, 200]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

print("\nMissing Values Count:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].fillna(df["Score"].median())
print("\nAfter Imputing Missing Values:")
print(df)

print("\nDuplicate Rows Count:", df.duplicated().sum())
df = df.drop_duplicates()
print("\nAfter Dropping Duplicates:")
print(df)

q1 = df["Score"].quantile(0.25)
q3 = df["Score"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

df_clean = df[(df["Score"] >= lower_bound) & (df["Score"] <= upper_bound)]
print("\nAfter Removing Outliers:")
print(df_clean)
