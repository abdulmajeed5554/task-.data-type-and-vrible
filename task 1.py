
Task number 1 : Python Varaibles and Data Types .
Question No :: 01
• Declare and initialize two variables, num1 and num2, with integer values. Calculate and print their sum

num1 = 5
num2 = 8
# calculate and print their sum

sum_result = num1 + num2

print('The sum of ',num1, "and",num2,"is:",sum_result)
The sum of 5 and 8 is: 13

Question no :: 02

. Create a variable, message, and assign it a string value. Append another string, " World!", to it and print the result.

message = "Hello"

message += " World!"

print(message)
Hello World!
Question No :: 03
• Define a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun.

# create a variable assing a boolean value
is_python_fun = True    # or assing a False value than print("python is not a fun")

# print a statement based that python considerd a fun
if is_python_fun:
    print("Python is a fun.")
else:
    print("Python is not a fun.")
Python is a fun.
Question No :: 04
• Create a list, fruits, with three different fruit names. Print the list and then add a new fruit to it. Print the updated list

# Create a list of fruits

Fruits = ["Apple","Mango","Banana"]

# orignal fruits list
print("Original fruits list : ",Fruits)

# Add a new furits in the list
Fruits.append("Orange")

# updata list
print("Updata list is : ",Fruits)
Original fruits nlist :  ['Apple', 'Mango', 'Banana']
Updata list is :  ['Apple', 'Mango', 'Banana', 'Orange']
Question No :: 05
• Declare a variable, price, with a floating-point value. Convert it to an integer and print both the original and converted values.

# create a variable floating value.
value = 5.6

# print original value
print("Original value is :",value)

# Convert value into integer
integer_value = int(value)

# print converted value.
print("Converted value is that :",integer_value)
Original value is : 5.6
Converted value is that : 5
Question No :: 06
• Create a dictionary, student_info, with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary.

# create a dictionary,student_info, with keys for "name","age","grade".
student_info = {
    "name":"abdul majeed",
    "age" : 18,
    "grade": "A"
}
# print dictionary
print("student_Information :",student_info)
student_Information : {'name': 'abdul majeed', 'age': 20, 'grade': 'A'}
Question No :: 07
• Write a program that takes user input for their age and prints a message addressing their age group (e.g., "Teenager," "Adult").

# create user input for thier age
user = int(input("Enter you age : "))
# check if user age is teenager or adult
if user <= 20:
    print("You are  Teenager")
else:
    print("You are Adult")
Enter you age : 8
You are  Teenager
Question No :: 08
• Define a complex number variable, comp_num, with a real and imaginary part. Print both parts separately

# create a complex number variable
comp_num = 6+5j
# print both parts separately real and imaginary .
print("Real part of complex number :",comp_num.real)
print("Imaginary part of complex number :",comp_num.imag)
Real part of complex number : 6.0
Imaginary part of complex number : 5.0
Question No :: 09
• Combine two strings using string concatenation, and then use string interpolation to include the length of the resulting string in a print statement.

# create a two variable and assing two string values.
str1 = "abdul "
str2 = " majeed"
# concatenation two string and there length is 
combine = str1 + str2
print(f"Combine string is that : \"{combine}\".Its lenght : {len(combine)}")
Combine string is that : "abdul majeed".Its lenght : 14
Queation No :: 10
• Create a tuple, days_of_week, with the names of the days. Access and print the third day of the week.

# Create a tuple
days_of_week = ("Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

# if you access and print the third dsy of the week.
third_day = days_of_week[2]
# print third day
print("Third day of the week is that ::",third_day)
Third day of the week is that :: Wednesday
 