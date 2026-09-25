Q1. Print name, age, college and branch

name = input("Enter your name:Sarthak Barde ")
age = input("Enter your age:18 ")
college = input("Enter your college name:RBU ")
branch = input("Enter your branch:ECS ")

print("\n--- Student Details ---")
print(f"Name:    {name}")
print(f"Age:     {age}")
print(f"College: {college}")
print(f"Branch:  {branch}")


Q2. Take name as input and greet the user 

name = input("Enter your name:Sarthak ")
print("Hello,", name + "!")


Q3.Take two numbers and display their sum

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)  


Q4.Perform all arithmetic operations on two numbers 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
    print("Floor Division =", num1 // num2)
    print("Modulus =", num1 % num2)
else:
    print("Division, Floor Division, and Modulus are not possible.")

print("Exponentiation =", num1 ** num2)


Q5. Calculate area of a circle 

import math

radius = float(input("Enter the radius of the circle: "))

area = 3.14 * radius ** 2

print("Area of the circle =", area)


Q6. Calculate simple interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


Q7. Convert Celsius to Fahrenheit 

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


Q8. Calculate total and percentage of 5 subjects

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
marks4 = float(input("Enter marks for subject 4: "))
marks5 = float(input("Enter marks for subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total / 5

print("Total marks =", total)
print("Percentage =", percentage, "%")


Q9. Swap two numbers

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1, num2 = num2, num1

print("After swapping:")
print("First number =", num1)
print("Second number =", num2)


Q10. Convert seconds into hours, minutes and seconds

seconds = int(input("Enter total seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)







