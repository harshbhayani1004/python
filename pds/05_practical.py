import csv

f = open("sample.txt", "w")
f.write("Harsh\nSSASIT Computer Engineering\n")
f.close()

f = open("sample.txt", "a")
f.write("PDS Practical\n")
f.close()

f = open("sample.txt", "r")
content = f.read()
print(content)
f.close()

f = open("students.csv", "w", newline="")
writer = csv.writer(f)
writer.writerow(["Enrollment", "Name", "Department", "Marks"])
writer.writerow([17, "Harsh", "Computer Engineering", 91])
writer.writerow([41, "Ashish", "IT", 87])
f.close()

f = open("students.csv", "a", newline="")
writer = csv.writer(f)
writer.writerow([18, "Meet", "BCA", 74])
f.close()

f = open("students.csv", "r")
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()

f = open("data.bin", "wb")
data = b'hello'
f.write(data)
f.close()

f = open("data.bin", "ab")
f.write(b'world')
f.close()

f = open("data.bin", "rb")
bin_content = f.read()
print(bin_content)
f.close()
