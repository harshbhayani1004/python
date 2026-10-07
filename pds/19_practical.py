import pandas as pd

df1 = pd.DataFrame({
    "Roll": [17, 41, 18],
    "Name": ["Harsh", "Ashish", "Meet"],
    "Dept": ["Computer Engineering", "IT", "Computer Engineering"],
    "Marks": [91, 87, 74]
})

df2 = pd.DataFrame({
    "Roll": [4, 7],
    "Name": ["Taksh", "Aryan"],
    "Dept": ["IT", "Computer Engineering"],
    "Marks": [81, 68]
})

df = pd.concat([df1, df2], ignore_index=True)
print("Combined DataFrame:")
print(df)

sliced = df.iloc[1:4, 0:3]
print("\nSliced Data (rows 1-3, cols 0-2):")
print(sliced)

filtered = df[df["Marks"] >= 80]
print("\nFiltered Data (Marks >= 80):")
print(filtered)

sorted_df = df.sort_values(by="Marks", ascending=False)
print("\nSorted Data (by Marks descending):")
print(sorted_df)

aggregated = df.groupby("Dept")["Marks"].agg(["mean", "max", "min"])
print("\nAggregated Data by Dept:")
print(aggregated)

df["Norm_Marks"] = (df["Marks"] - df["Marks"].min()) / (df["Marks"].max() - df["Marks"].min())
print("\nNormalized Data (Min-Max 0 to 1):")
print(df[["Name", "Marks", "Norm_Marks"]])
