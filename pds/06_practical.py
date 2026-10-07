try:
    a = 10
    b = 0
    res = a / b
    print(res)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    num = int("abc")
except ValueError:
    print("Invalid integer conversion")
else:
    print("Conversion successful")
finally:
    print("This block always runs")

class InvalidAgeError(Exception):
    pass

student_name = "Harsh"
age = 15
try:
    if age < 19 or age > 24:
        raise InvalidAgeError("Age must be between 19 and 24")
    print("Student:", student_name, "Age:", age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
