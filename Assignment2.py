#Task 1: Check if a Number is Even or Odd

Num = int(input("Enter the number: "))
if (Num%2==0):
    print(Num,"is an even number.")
else:
    print(Num,"is an odd number.")

#Task 2: Sum of Integers from 1 to 50 Using a Loop

Sum = 0
for i in range(1,51):
    Sum +=i 
print("Sum of numbers from 1 to 50 is:",Sum)