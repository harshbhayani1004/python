num = 10
if num > 0:
    print("Positive number")

n = 7
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

marks = 81
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

count = 1
while count <= 5:
    print(count)
    count += 1

subjects = ["MPI", "CN", "PDS"]
for s in subjects:
    print(s)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

for x in range(1, 6):
    if x == 4:
        break
    print(x)

for y in range(1, 6):
    if y == 3:
        continue
    print(y)

for z in range(1, 4):
    if z == 2:
        pass
    print(z)
