import pandas as pd

s = pd.Series([74, 81, 87, 91], index=["MPI", "CN", "WAD", "PDS"])
print(s)
print(s["CN"])

data = {
    "Name": ["Harsh", "Ashish", "Meet", "Taksh", "Darsh"],
    "Dept": ["Computer Engineering", "IT", "Computer Engineering", "IT", "Computer Engineering"],
    "Marks": [91, 87, 74, 81, 68],
    "Attendance": [95, 88, 75, 82, 70]
}

df = pd.DataFrame(data)
print(df)

print(df["Name"])
print(df[["Name", "Marks"]])
print(df.iloc[0:2])
print(df.loc[df["Dept"] == "Computer Engineering", ["Name", "Marks"]])

filtered_df = df[df["Marks"] > 80]
print(filtered_df)

print(df.groupby("Dept")["Marks"].mean())
print(df.groupby("Dept")["Marks"].agg(["mean", "max", "min", "count"]))
