import math
import random
import statistics

def add(a, b):
    return a + b

def greet(name, msg="Hello"):
    print(msg, name)

def student_info(name, age):
    print("Name:", name, "Age:", age)

def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def print_details(**data):
    for k, v in data.items():
        print(k, ":", v)

print(add(10, 20))

greet("Harsh")
greet("Ashish", "Welcome")

student_info(age=20, name="Harsh")

print(sum_all(1, 2, 3, 4, 5))

print_details(name="Harsh", college="SSASIT", dept="Computer Engineering", enrollment=17)

print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2, 3))

print(random.randint(1, 10))
print(random.choice(["MPI", "CN", "PDS", "WAD"]))

nums = [55, 68, 74, 81, 87]
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))
