#Task1 :Calculate Factorial Using a Function 
def factorial(n):
    if n<=1:
        return 1
    else:
        return n * factorial (n-1)

num = int(input("Enter the number : "))
Result = factorial(num)
print("Factorial of number is",Result)

#Task 2: Using the Math Module for Calculations
import math
num = int(input("Enter the number: "))
print("Square root of number",num, "is: ",math.sqrt(num))
print("logerithm of number",num, "is: ",math.log(num))
print("sine of number",num, "is: ",math.sin(num))   
