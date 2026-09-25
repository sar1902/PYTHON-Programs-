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


Q11. Check whether a number is positive, negative or zero 
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


Q12. Check whether a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


Q13. Check whether a person is eligible to vote

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

Q14. Find greater of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Greater number =", num1)
elif num2 > num1:
    print("Greater number =", num2)
else:
    print("Both numbers are equal")


Q15. Find greatest of three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Greatest number =", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest number =", num2)
else:
    print("Greatest number =", num3)


Q16. Check whether a year is a leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


Q17. Check whether a number is divisible by 5 and 11

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")

Q18. Check whether a number lies between 10 and 50

num = int(input("Enter a number: "))

if 10 <= num <= 50:
    print("The number lies between 10 and 50")
else:
    print("The number does not lie between 10 and 50")


Q19. Simple calculator using  if/elif

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

Q20. 








