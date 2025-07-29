#Task1: Read a File and Handle Errors

try:
    with open('Sample.txt','r') as file1:
        return_file = file1.readlines()
        print("line1:",return_file[0])
        print("line2:",return_file[1])
        file1.close()
except FileNotFoundError :
    print("The file is not found")

#Task2: Write and Append Data to a File

file = open('Sample.txt','a')
print("Enter text to write to the file: ")
appending_file = file.write('Hello,python!\n')
print("Data is succesfully written to Sample.txt!")
print("Enter another text to append")
appending_file = file.write('Learning file handling in the python.')
print("Data succesfully appended")
file.close()

file = open('Sample.txt','r')
reading_file = file.read()
print(reading_file)
file.close()