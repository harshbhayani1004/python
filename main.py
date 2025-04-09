#This Is My First Program
print("Hello")

#variable.(string , float , integer , boolean).

#strings
first_name = "harsh"
food  = "pizza"
email = "harshbhayani77@gmail.com"
print(f"Hello {first_name}")
print(f"my fev food is {food}")
print(f"my email is :{email}")

#integers.
age = 18
quantity = 3
num_of_student= 30
print(f"you are {age} year old")
print(f"you are buying {quantity} apple")
print(f"your class have {num_of_student} student")

#float
price = 99.99
print(f"The price is ${price}")

#boolean

is_student = False
if is_student:
    print("you are a student")
else:
    print("you are not student")

x = int(input("enter the 1st value :"))
y = int(input("enter the 2nd value :"))

print(f"sum of {x} and {y} :" , x+y)

# #typecasting = the process of converting a value of one data type to another
#               (string,int,float,bool)
#              explicit vs implicit
from statistics import quantiles
import math

#        this is explicit       #
name = 'harsh'
age = 18
spi = 3.3
student = True

name = bool(name)
print(name)

 #        this is implicit       #

x = 2
y = 2.0

x = x/ y

print(x)

name = input("enter your name :")
age = int(input("enter your age:"))
age = age + 1
print(f"Hello {name}")
print(f"you are {age} old")
adjective1 = input("enter an adjective for describe zoo :")
noun = input("enter a noun :")
adjective2 = input(f"enter the adjective for describe {noun}:")
verb =  input(f"enter a verb for {noun}:")
adjective3 = input("enter an adjective :")


print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

#find the rectengel area.

length_of_rectengel = float(input("enter the value of length :"))
breadth_of_rectengel = float(input("enter the value of breadth :"))
height_of_rectengel = float(input("enter the value of height :"))
area = length_of_rectengel * breadth_of_rectengel * height_of_rectengel
print(f"the volume of rectengel is : {area} cm^3")

item = input("what is item would you like to buy? :")
price = float(input("what is the price? : "))
quantity = int(input("how much quantity? :"))

print(f"Total price is : $" ,price * quantity)


#maths function.

x = 3.14
y = -4
z = 5

result = round(x) # float value into int.
result = abs(y) #value into 0 to (+infinite)
result = pow(z , 2) #pow is power function
result = max(x , y, z)#find max value
result = min(x, y, z)#find min value

print(result)

x = 9.8

import math
print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x)#exet value + 1 ===>  9.1 = 10
result = math.floor(x) #exet value ===>  9.9 = 9

print(result)

#c = 2*(pi)*r

import math

R = float(input("enter the value of R:"))
print("the value of area is:" ,2*R*math.pi)

# a = pi*r^2
import math

r = int(input("enter the value of r:"))
print("the value of A is :" , pow(r , 2) * math.pi)

# c = rout of a^2 + b^2
A = float(input("enter the value of A :"))
B = float(input("enter the value of B :"))

print("value of C is :" ,math.sqrt(pow(A ,2)+pow(B , 2)))


#  if, else, elif  ####

age = int(input("enter your age :"))

if age >= 18:
    print("you can vote")
elif age <= 0:
    print("you aren't exist in real life!")
else :
    print("wait and watch!")


responses = input("would you like food ? (Y/N) :")

if responses == "Y":
    print("have some food!")
else :
    print("no food for you")

for_sale = True

if for_sale:
    print("item for sale")
else:
    print("item not for sale")
