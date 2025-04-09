math = input("would you like (+, -, *, /) : ")
num1 = float(input("Enter the value of num1 :"))
num2 = float(input("Enter the value of num2 :"))

if math == "+":
    result = (num1 + num2)
elif math == "-":
    result = (num1 - num2)
elif math == "*":
    result = (num1 * num2)
elif math == "/":
    result = (num1 / num2)
else:
    result = "not exist"
    print(f"{math} doesn't exist")

print(f"calculation :({num1} {math} {num2}) = {result}")