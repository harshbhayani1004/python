import pandas as pd
import statistics

df = pd.read_csv("employee - employee.csv")

data = df["Age"].tolist()

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Variance:", statistics.variance(data))
print("Standard Deviation:", statistics.stdev(data))
print("Range:", max(data) - min(data))

q1 = df["Age"].quantile(0.25)
q2 = df["Age"].quantile(0.50)
q3 = df["Age"].quantile(0.75)

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("IQR:", q3 - q1)