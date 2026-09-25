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





