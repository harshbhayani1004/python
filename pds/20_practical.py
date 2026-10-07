import matplotlib.pyplot as plt

study_hours = [1, 2, 4, 6, 8]
marks = [55, 62, 74, 87, 95]

subjects = ["MPI", "CN", "SS", "WAD", "PDS"]
subject_marks = [74, 81, 68, 87, 91]

scores = [55, 62, 68, 74, 74, 81, 87, 87, 91, 91, 95, 95]

departments = ["Computer Engineering", "IT", "BCA", "Civil Engineering"]
student_count = [60, 45, 30, 25]

height = [160, 165, 170, 172, 175, 180]
weight = [55, 60, 65, 68, 72, 78]

fig = plt.figure(figsize=(12, 8))
fig.suptitle("Matplotlib Student Data Visualization Plots", fontsize=16)

plt.subplot(2, 3, 1)
plt.plot(study_hours, marks, color="blue", marker="o")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.bar(subjects, subject_marks, color="orange")
plt.title("Subject Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.subplot(2, 3, 3)
plt.hist(scores, bins=5, color="green", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")

plt.subplot(2, 3, 4)
plt.pie(student_count, labels=departments, autopct="%1.1f%%", colors=["skyblue", "pink", "yellow", "lightgreen"])
plt.title("Students by Department")

plt.subplot(2, 3, 5)
plt.scatter(height, weight, color="red")
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

plt.tight_layout()
plt.savefig("20_plots.png")
plt.show()
