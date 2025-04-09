unit_choice = input("Enter the celcius or fehrenheit (choice : C/F) = ")
temp = float(input(f"Enter the value of {unit_choice} :"))

if unit_choice == "C":
    result = (temp*(9/5)) + 32
    
    print(f"the conversion {unit_choice} to F : {result} ")

elif unit_choice == "F":
    result = (temp -32)*(5/9)
    
    print(f"the conversion {unit_choice} to C : {result} ")

else :
   print("Please cheak your unit!")