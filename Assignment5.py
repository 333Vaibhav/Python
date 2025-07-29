#Task 1: Create a Dictionary of Student Marks

students = {
    'vaibhav':40,
    'parth':90,
    'jay':80
    }
name = input("Enter the student name: ")
if name in students:
    print("Marks of",name,"is:",students[name])
else:
    print("student not found")

#Task 2: Demonstrate List Slicing 

Num_list = list(range(1,11))
First_five_element = Num_list[0:5]
Reverse_first_five_element = First_five_element[::-1]
print("list:",Num_list)
print("First Five Element:",First_five_element)
print("Reverse First Five Element:",Reverse_first_five_element)